# How-to: Spreadsheet to CSV to YAML (.yml) file
### *(Please note that this documentation is currently under construction.)*  
## Recording item information
Create a copy of **[this template](https://docs.google.com/spreadsheets/d/1tXg4p4iouy6OBnflIgYaC_AVBDDvhF_pym7eYVc6RMc/edit?usp=sharing)**. Fill in the required item information as detailed below.  

- By entering information for multiple items in successive rows, multiple YAML files may be generated at once.
- To prevent any alteration to date formats, etc., which would prevent processing, apply plain-text formatting to all cells in the data-entry spreadsheet.
- An example spreadsheet complete with input values is available [here](https://docs.google.com/spreadsheets/d/1ixc8uVCmZAgtEU8S446XntZoeRVsCPcLSX_R-KnLD_4/edit?usp=sharing).
- Example output YAML files--both generated from the sample spreadsheet above--are available **[here](https://drive.google.com/a/uw.edu/file/d/1XL9BSejpJKPZbwVYZAmtgE4CiJe2pRmT/view?usp=sharing)** and **[here](https://drive.google.com/a/uw.edu/file/d/1MNK9B0tXiLXbOJW8AZ6pKKT5b-7uj5NY/view?usp=sharing)**. Note that YAML files output by the script will have the file extension ".yml", not "_YAML.txt" as with these sample files.
- Much of the documentation below has been taken directly from [ruthtillman's](https://github.com/ruthtillman) [yaml-generator-for-hathitrust](https://github.com/ruthtillman/yaml-generator-for-hathitrust) repository, which is the source of the Python script used here.
- Column headings in ALL CAPS below (FRONT_COVER, COPYRIGHT, etc.) are HathiTrust page tags, and image file numbers input in these columns will be tagged as such. The page-tag information given below was taken directly from a HathiTrust-provided example YAML file available **[here](https://drive.google.com/file/d/0B0EHs5JWGUMLWjU2OHVhQzN5WEk/view)**.  (The example YAML file is linked to from the [HathiTrust Cloud Validation and Packaging Service document](https://docs.google.com/document/d/1OQ0SKAiOH8Xi0HVVxg4TryBrPUPtdv4qA70d8ghRltU/edit?usp=sharing).
- It is important to remember that anytime you enter a number in the spreadsheet to indicate a captured page image or images, you are entering the number(s) for an *image file* or set of *image files*, **not** for pages in a book or document, the numbering of which will of course differ from that of image files. 
- When entering image numbers in the spreadsheet, exclude leading zeros and filename extensions. For example, to input 00000001.tif, in the FRONT_COVER column, enter "1".

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
| Compression Date YYYY-MM-DD | Enter "N" if captured images were not compressed. |
| Compression Time HH:MM | Enter "N" if captured images are uncompressed. |
| Compression DST: Y/N | Enter "N" if captured images are uncompressed. |
| Compression Tool(s) | Enter "N" if captured images are uncompressed. |
| Scanning Order ("Y"=L->R)) | Enter "Y" for books that were scanned from left to right. *See [note 2](https://github.com/ries07uw/HathiTrustYAMLgenerator/blob/master/HowTo.md#notes) below.*|
| Reading Order ("Y"=L->R) | Enter "Y" for books that should be read from left to right. *See [note 2](https://github.com/ries07uw/HathiTrustYAMLgenerator/blob/master/HowTo.md#notes) below.* |
| Filename extension | Enter filename extension of the image files here. (Examples: "tif", "jpg") |
| Total number of images | Enter the total number of image files included in the item here. |
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
  
## Generating a YAML file for upload
- Download the sheet with input values in CSV format.
- To prevent any alteration to date formats, etc., which would prevent processing, open the downloaded CSV file in a simple text-editing program such as [Notepad++](https://notepad-plus-plus.org/).
- Delete column headers--all content coming before the first digit of the first item's barcode--from the CSV file, and save changes. 
- STEPS FOR USING SCRIPT HERE
- If images are uncompressed, the *image_compression_date*, *image_compression_agent*, and *image_compression_tool* lines should be deleted from output YAML files prior to upload. (See [notes regarding needed improvements](NeededImprovements.md).)

### Notes:  
1. Quotation marks are used above to indicate specific values for entry, but should *not* be entered in the spreadsheet.
2. From yaml-generator-for-hathitrust, [field_guide.md](https://github.com/ruthtillman/yaml-generator-for-hathitrust/blob/master/field_guide.md):  
   - **Important Note:** While HathiTrust can handle books where the last page or back cover is 00000001, this YAML output tool can only handle "normal" English reading order if books were scanned in the same direction as they should be read. i.e. if they should be read right-to-left, then it can handle a right-to-left scan, but it can't handle a book read left-to-right but scanned right-to-left. 
