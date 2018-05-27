# How-to: CSV to YAML  
### *(Please note that this documentation is currently under construction.)*  

Create a copy of [this template](https://docs.google.com/spreadsheets/d/1tXg4p4iouy6OBnflIgYaC_AVBDDvhF_pym7eYVc6RMc/edit?usp=sharing). Fill in the required item information as detailed below.  

- An example spreadsheet complete with input values is available HERE--NEED LINK.
- An example output YAML file is available HERE--NEED LINK.
- Much of the documentation below has been taken directly from [ruthtillman's](https://github.com/ruthtillman) [yaml-generator-for-hathitrust](https://github.com/ruthtillman/yaml-generator-for-hathitrust) repository, which is the source of the Python script used here.
- Information regarding conventions for the use of page tags (in ALL CAPS in the table below) was taken directly from HathiTrust documentation available [here](https://drive.google.com/file/d/0B0EHs5JWGUMLWjU2OHVhQzN5WEk/view).  

| Column Heading | Input Instructions |
| --- | --- |
| Item barcode | UW-assigned item barcode (beginning 393520...) for the digitized item. In this context, an "item" may be defined as a book, document, set of documents, etc. having a single assigned barcode. |
| Scan Date YYYY-MM-DD | Enter the date (the first date, if more than one) of digital capture here. Be sure to enter as shown in the column heading. This value can be taken from the "date created" value shown for the first captured image file of a given item. |
| Scan Time HH:MM | Enter the start time of digital capture here. Be sure to enter as shown in the column heading. This value can be taken from the "date created" value shown for the first captured image file of a given item. |
| Scan DST: Y/N | If the item was captured during daylight savings time enter "Y", if not enter "N". |
| "Y" if using BookDrive / If not, enter scanner maker | Entering "Y" will output the value "Atiz" in the "scanner_make" line of the output YAML file. If you are not using the Atiz BookDrive for capture, enter the manufacturer of the scanner or other digital capture device you are using. (Example: "Epson") |
| "Y" if using BookDrive / If not, enter scanner model | Entering "Y" will output the value "BookDrive Mark II" in the "scanner_model" line of the output YAML file. If you are not using the Atiz BookDrive for capture, enter the model of the scanner or other digital capture device you are using. (Example: "Expression 12000XL") |
| Bitone DPI | If the item was captured in black-and-white, enter the capture DPI value here. |
| Contone DPI | If the item was captured in color or greyscale, enter the capture DPI value here. |
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
  
#### Preparing downloaded CSV file for processing  


### Notes:  
- Quotation marks are used above to indicate specific values for entry, but should *not* be entered in the spreadsheet.
- ADD NOTES ABOUT COMPRESSION FIELDS / MANUAL DELETION / NEED FOR SCRIPT IMPROVEMENT HERE.
