<p align="right">
   <img width="176" height="60" alt="INP logo" src="media/inplogo.jpg" />
   <img width="176" height="60" alt="NFDI4BIOIMAGE logo" src="media/nfdi4bioimagelogo.png">
</p>

<!--
[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.1234567.svg)](https://doi.org/10.5281/zenodo.1234567)
-->

# Bioimaging Data Management Workflow for Plasma Medicine
This repository contains the Jupyter notebook implementation of a bioimaging data management workflow for plasma medicine (see [preprint](https://doi.org/10.64898/2026.01.26.700509 ) and [poster](https://doi.org/10.5281/zenodo.16412003)). The workflow is implemented as a structured pipeline integrating open-source tools, including  [OMERO](https://www.openmicroscopy.org/omero/) for image data management, [eLabFTW](https://www.elabftw.net/) as an electronic laboratory notebook, [Adamant](https://github.com/plasma-mds/adamant) for schema-driven metadata collection, and [Micro-Meta App](https://wu-bimac.github.io/MicroMetaApp.github.io/) for standardized documentation of microscopy acquisition settings that are connected via programming interfaces to enable persistent linkage of metadata to image datasets using standardized annotations.

<!--
## Changelog
### [x.x.x] January 26, 2026
* Initial release of the GitHub repository
-->

## Set up
A [JupyterLab](https://jupyter.org) environment is required to run the provided [notebook](workflow.ipynb).
The workflow was designed and tested on Python 3.12.5.
Follow the [installation guideline](https://jupyter.org/install) for support.

## Dependencies 
The following list summarizes the key dependencies:
* [**Elabapi**](https://pypi.org/project/elabapi-python/)
* [**OMERO-py**](https://pypi.org/project/omero-py/)
* [**Openpyxl**](https://pypi.org/project/openpyxl/)
* [**Pandas**](https://pypi.org/project/pandas/)

## Usage
To use the provided Jupyter notebook, download [workflow.ipynb](workflow.ipynb) and the two Python scripts [omerohandler.py](scripts/omerohandler.py) and [elabftwapihandler.py](scripts/elabftwapihandler.py).
These files must be located in the same working directory.
To access the respective OMERO and eLabFTW instances, the host addresses must be adjusted in the respective handler scripts (see description below).

### eLabFTW
The codeline (l. 43) in elabftwapihandler.py has to be changed:
```
configuration.host = 'hostAdress'
```
the 'hostAdress' variable has to be replaced by the actual host url adress of your eLabFTW instance.

### OMERO
The codeline (l. 21) in omerohandler.py has to be changed:
```
conn = BlitzGateway(usrname, passwrd, host= hostAdress, port= hostPort, secure=True)
```
the 'hostAdress' variable has to be replaced by the actual host url adress of your OMERO instance.

The adjusted notebook can be accessed by opening the .ipynb file in a JupyterLab environment; in some local JupyterLab installations, double-clicking the downloaded, modified .ipynb file may be sufficient.

## Support
If you find a bug or need help, please open an issue. When reporting a bug, include the version, OS, steps to reproduce, expected vs actual behavior, and any logs or screenshots.

## How to cite
Ahmadi M, Wagner R, Bekeschus S, Becker MM, Bioimaging Data Management Workflow for Plasma Medicine. BioRxiv. 2026; DOI: 10.64898/2026.01.26.700509. 

## Grant information
The work is funded by the Deutsche Forschungsgemeinschaft (DFG, German Research Foundation) under the National Research Data Infrastructure – NFDI 46/1 – 501864659.

<img width="400" alt="image" src="media/dfglogoschriftzugblaufoerderungen.gif" />

