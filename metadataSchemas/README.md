# Metadata schemas for screen objects in OMERO

The json schema based file [ScreenSchema.json](ScreenSchema.json) contains all important fields for the OMERO annotation carried out by the Jupyter workflow.

The Screen_schema.json contains a file upload field for the biological metadata (which are used to annotate the individual wells), the Jupyter workflow considers a Excel file upload. The template for such a Excel file is provided in [biologicalMetadata.xlsx](biologicalMetadata.xlsx).

Plasma metadata are collected with the plasma metadata schema [Plasma-MDS](https://github.com/plasma-mds/plasma-metadata-schema).
