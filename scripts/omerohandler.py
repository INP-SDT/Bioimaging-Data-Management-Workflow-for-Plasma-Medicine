# -*- coding: utf-8 -*-
"""
Created on Fri May 17 12:13:44 2024

@author: WagnerR
"""
import omero
import json
from omero.gateway import BlitzGateway, DatasetWrapper, ProjectWrapper
import tkinter as tk
from tkinter import simpledialog, filedialog
import os

# %% log into OMERO using Jupyter notebooks
"""
To use this handler script please exhange 'hostAdress' by the url of your OMERO instance and 'hostPort' by your port 
"""
def Omero_login_Jupyter(usrname, passwrd):
    # setup for omero connection
    try:
        conn = BlitzGateway(usrname, passwrd, host= hostAdress, port= hostPort, secure=True)
        conn.connect()
        print("Connected to OMERO")
    except AttributeError:
        print("Connection not possible")
        exit()
    return conn



# %%
"""
delete_annotation() deletes any Annotation based on their annotation_id
"""
def delete_annotation(conn, ID: int):
    delete = conn.getObject("Annotation", ID)
    conn.deleteObjects("Annotation", [delete.id])

# %%

def annotate_screen(conn, screenName, jsonData):
    screenList = conn.getObjects("Screen")
    for screen in screenList:
        if screen.getName() == screenName:
            print("Screen", screenName, "found and matched")
            try:
                jsonData["screen"]     
                # add newKeyValuePairs to an empty annotation list
                map_ann = omero.gateway.MapAnnotationWrapper(conn)
                # Use 'client' namespace to allow editing in Insight & web
                map_ann.setNs("Screen metadata")
                # initialize boolean for switch from empty to filled map annotation
                noMapAnnotationYet = True
                for key, value in jsonData["screen"].items():
                    if key == "plate":
                        continue
                    else:
                        if key == "biologicalMetadata":
                            continue
                        else:
                            newKeyValuePair = [(key, str(value))]
                            if noMapAnnotationYet == True:
                                map_ann.setValue(newKeyValuePair)
                                noMapAnnotationYet = False
                            else:
                                map_ann.setValue(map_ann.getValue() + newKeyValuePair)        
            except KeyError:
                pass        
            screen.linkAnnotation(map_ann)
    print("Screen metadata are linked to screen: " + screenName) 
        
# %% 

def annotate_plate(conn, plateName, jsonData, excelData, wellBool: bool = False):
    plateList = conn.getObjects("Plate")
    for plate in plateList:
        if plate.getName() == plateName:
            print("Plate", plateName, "found and matched")
            try:
                jsonData["screen"]["plate"]  
                # add newKeyValuePairs to an empty annotation list
                map_ann = omero.gateway.MapAnnotationWrapper(conn)
                # Use 'client' namespace to allow editing in Insight & web
                map_ann.setNs("Plate metadata")
                # initialize boolean for switch from empty to filled map annotation
                noMapAnnotationYet = True
                for key, value in jsonData["screen"]["plate"].items():
                    if key == "plateDescription":
                        for key, value in jsonData["screen"]["plate"]["plateDescription"].items():
                            if key == "cellInformation":
                                for key, value in jsonData["screen"]["plate"]["plateDescription"]["cellInformation"].items():
                                    if key == "strainIdentity":
                                        for key, value in jsonData["screen"]["plate"]["plateDescription"]["cellInformation"]["strainIdentity"].items():
                                            newKeyValuePair = [(key, str(value))]
                                            #print("Strain ", newKeyValuePair)
                                            if noMapAnnotationYet == True:
                                                map_ann.setValue(newKeyValuePair)
                                                noMapAnnotationYet = False
                                            else:
                                                map_ann.setValue(map_ann.getValue() + newKeyValuePair)
                                    elif key == "cultureMedia":
                                        for key, value in jsonData["screen"]["plate"]["plateDescription"]["cellInformation"]["cultureMedia"].items():
                                            if key == "additives":                                
                                                # dissect list from array into key value pairs
                                                additivesDict = {}
                                                for index, entry in enumerate(jsonData["screen"]["plate"]["plateDescription"]["cellInformation"]["cultureMedia"]["additives"], start=1):
                                                    #newKeyValuePair = [[f"Additive {index}"] = entry['additives']]
                                                    additivesDict[f"Additive {index}"] = entry['additives']
                                                    additivesDict[f"volumeOfAdditives {index}"] = str(entry['volumeOfAdditives'])
                                                    
                                                for key, value in additivesDict.items():
                                                #for key, value in jsonData["screen"]["plate"]["plateDescription"]["cellInformation"]["cultureMedia"]["additives"].items():
                                                    newKeyValuePair = [(key, str(value))]
                                                    #print("additives ", newKeyValuePair)
                                                    if noMapAnnotationYet == True:
                                                        map_ann.setValue(newKeyValuePair)
                                                        noMapAnnotationYet = False
                                                    else:
                                                        map_ann.setValue(map_ann.getValue() + newKeyValuePair)
                                                
                                            else:
                                                newKeyValuePair = [(key, str(value))]
                                                #print("Media", newKeyValuePair)
                                                if noMapAnnotationYet == True:
                                                    map_ann.setValue(newKeyValuePair)
                                                    noMapAnnotationYet = False
                                                else:
                                                    map_ann.setValue(map_ann.getValue() + newKeyValuePair)
                                            
                                    else: 
                                        newKeyValuePair = [(key, str(value))]
                                        #print(newKeyValuePair)
                                        if noMapAnnotationYet == True:
                                            map_ann.setValue(newKeyValuePair)
                                            noMapAnnotationYet = False
                                        else:
                                            map_ann.setValue(map_ann.getValue() + newKeyValuePair)
                            else: 
                                newKeyValuePair = [(key, str(value))]
                                #print(newKeyValuePair)
                                if noMapAnnotationYet == True:
                                    map_ann.setValue(newKeyValuePair)
                                    noMapAnnotationYet = False
                                else:
                                    map_ann.setValue(map_ann.getValue() + newKeyValuePair)
                    else:
                        newKeyValuePair = [(key, str(value))]
                        #print(newKeyValuePair)
                        if noMapAnnotationYet == True:
                            map_ann.setValue(newKeyValuePair)
                            noMapAnnotationYet = False
                        else:
                            map_ann.setValue(map_ann.getValue() + newKeyValuePair)
            except KeyError:
                pass        

            # second case for existence of Plasma-MDS metadata
            try:
                jsonData["source"]["name"] 
                # add newKeyValuePairs to an empty annotation list
                map_ann_plas = omero.gateway.MapAnnotationWrapper(conn)
                # Use 'client' namespace to allow editing in Insight & web
                map_ann_plas.setNs("Plasma metadata")
                # initialize boolean for switch from empty to filled map annotation
                noMapAnnotationYet = True
                for key, value in jsonData["source"].items():
                    newKeyValuePair = [(key, str(value))]
                    if noMapAnnotationYet == True:
                        map_ann_plas.setValue(newKeyValuePair)
                        noMapAnnotationYet = False
                    else:
                        map_ann_plas.setValue(map_ann_plas.getValue() + newKeyValuePair)
                for key, value in jsonData["medium"].items():
                    newKeyValuePair = [(key, str(value))]
                    if noMapAnnotationYet == True:
                        map_ann_plas.setValue(newKeyValuePair)
                        noMapAnnotationYet = False
                    else:
                        map_ann_plas.setValue(map_ann_plas.getValue() + newKeyValuePair)
                for key, value in jsonData["target"].items():
                    newKeyValuePair = [(key, str(value))]
                    if noMapAnnotationYet == True:
                        map_ann_plas.setValue(newKeyValuePair)
                        noMapAnnotationYet = False
                    else:
                        map_ann_plas.setValue(map_ann_plas.getValue() + newKeyValuePair)
                for key, value in jsonData["diagnostics"].items():
                    newKeyValuePair = [(key, str(value))]
                    if noMapAnnotationYet == True:
                        map_ann_plas.setValue(newKeyValuePair)
                        noMapAnnotationYet = False
                    else:
                        map_ann_plas.setValue(map_ann_plas.getValue() + newKeyValuePair)
            except KeyError:
                pass  
            
            plate.linkAnnotation(map_ann)
            plate.linkAnnotation(map_ann_plas)
            
            print("Plate metadata are linked to plate: " + plateName)
            
            if wellBool == True:
                # annotate the wells of the given plate
                            # Create the dictionary
                            result_dict = {
                                row[0]: 
                                    {
                                        str(excelData.iloc[0, i]): row[i] for i in range(1, len(excelData.columns))  # Dynamically iterate over all columns except the first
                                    }
                                for _, row in excelData.iloc[1:].iterrows()  # Skip the first row (headers)
                            }
                                
                            filtered_result_dict = {
                            key: value
                            for key, value in result_dict.items()
                            if any(v is not None for v in value.values())  # Keep only if at least one value is not None
                            }
                            for well in plate.listChildren():
                                #encodes row index as letter, 0 = A, 1 = B, ..., 7 = H
                                indexToLetter = lambda index: chr(65 + index) if 0 <= index <= 7 else None
                                wellName = indexToLetter(well.row) + str(well.column+1)

                                # add newKeyValuePairs to an empty annotation list
                                well_map_ann = omero.gateway.MapAnnotationWrapper(conn)
                                noMapAnnotationYet = True
                                # Use 'client' namespace to allow editing in Insight & web
                                well_map_ann.setNs("Biological metadata")      
                                for key, value in filtered_result_dict[wellName].items():
                                    if value == None:
                                        continue
                                    else:
                                        newKeyValuePair = [(key, str(value))]
                                        if noMapAnnotationYet == True:
                                            well_map_ann.setValue(newKeyValuePair)
                                            noMapAnnotationYet = False
                                        else:
                                            well_map_ann.setValue(well_map_ann.getValue() + newKeyValuePair)
                                well.linkAnnotation(well_map_ann)
                            print("Wells of plate", plateName, "are annotated")

