# How-to: CSV to YAML  
### *(Please note that this documentation is currently under construction.)*  
## Creating a CSV file to document your item's structure and other information  
Use [this template](https://docs.google.com/spreadsheets/d/1tXg4p4iouy6OBnflIgYaC_AVBDDvhF_pym7eYVc6RMc/edit?usp=sharing) to fill in the necessary information about your digitized item.  

#### Information regarding template fields and how to enter data is given below.  
- Much of the documentation below has been taken directly from [ruthtillman's](https://github.com/ruthtillman) [yaml-generator-for-hathitrust](https://github.com/ruthtillman/yaml-generator-for-hathitrust) repository, which is the source of the Python script used here.
- Information regarding conventions for the use of page tags (in ALL CAPS in the table below) was taken directly from HathiTrust documentation available [here](https://drive.google.com/file/d/0B0EHs5JWGUMLWjU2OHVhQzN5WEk/view).  

| Column Heading | Input Instructions |
| --- | --- |
| Item barcode | UW-assigned item barcode (beginning 393520...) for the digitized item. In this context, an "item" may be defined as a book, document, set of documents, etc. having a single assigned barcode. |
| Scan Date YYYY-MM-DD | Enter the start time of digital capture here. This value can be taken from the "date created" field of the first captured image file for a given item. |
| Scan Time HH:MM | |
| Scan DST: Y/N | |
| "Y" if using BookDrive / If not, enter scanner maker | |
| "Y" if using BookDrive / If not, enter scanner model | |
| Bitone DPI | |
| Contone DPI | |
| Compression Date YYYY-MM-DD* | |
| Compression Time HH:MM* | |
| Compression DST: Y/N | |
| Compression Tool(s) | |
| Scanning Order (L->R) | |
| Reading Order (L->R) | |
| Filename extension | |
| Total number of images | |
| FRONT_COVER | |
| TITLE_PARTS | |
| TITLE | |
| COPYRIGHT | |
| TABLE_OF_CONTENTS | |
| Roman Numeral Start | |
| End Roman Numerals | |
| PREFACE | |
| Page 1 | |
| FIRST_CONTENT_CHAPTER_START | |
| CHAPTER_PAGE | |
| CHAPTER_START | |
| Final Page | |
| BLANK | |
| Unpaginated | |
| IMAGE_ON_PAGE | |
| FOLDOUT | |
| INDEX | |
| REFERENCES | |
| MULTIWORK_BOUNDARY | |
| BACK_COVER | |

### Notes:  
* ADD NOTES ABOUT COMPRESSION FIELDS / MANUAL DELETION / NEED FOR SCRIPT IMPROVEMENT HERE.
