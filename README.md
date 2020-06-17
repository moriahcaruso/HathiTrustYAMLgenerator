# YAMLgenerator  

## Python script and documentation adapted from [yaml-generator-for-hathitrust](https://github.com/ruthtillman/yaml-generator-for-hathitrust) created by [ruthtillman](https://github.com/ruthtillman)  

### This repository includes a Python script which uses an input CSV file to generate a YAML metadata file or files for uploading material to the **[HathiTrust digital library](https://www.hathitrust.org/)**.  
The purpose of adapting the Python script and documentation from the GitHub repository referenced above was to customize them for use at the **[University of Washington Libraries Preservation Services](http://www.lib.washington.edu/preservation)** unit.  

### The overall workflow is as follows, and is detailed in the **[how-to](https://github.com/ries07uw/HathiTrustYAMLgenerator/blob/master/HowTo.md)** file provided in this repository:
- **[Python 3.x](https://www.python.org/downloads/)** must be installed on the computer that will be used to generate YAML files, and the **[csv-to-yml.py](https://github.com/moriahcaruso/HathiTrustYAMLgenerator/blob/master/csv-to-yml.py)** script will need to be downloaded as well.  
- Create a copy of the **[data-entry spreadsheet template](https://drive.google.com/open?id=1tXg4p4iouy6OBnflIgYaC_AVBDDvhF_pym7eYVc6RMc)** and enter information about the digitized item, the digital capture process, etc. 
- Save the completed spreadsheet containing information about one or more digitized items as a CSV file.
- Run the [csv-to-yml.py](https://github.com/moriahcaruso/HathiTrustYAMLgenerator/blob/master/csv-to-yml.py) script 
- When prompted, enter the filepath to the saved CSV file.
- Whe, prompted, enter the filepath where generated YAML files should be saved.
- Confirm generated files and package along with page image files, OCR files, etc. for upload to the HathiTrust.  

### Next: [How to record item information in a spreadsheet and process this information to generate YAML files](HowTo.md).
