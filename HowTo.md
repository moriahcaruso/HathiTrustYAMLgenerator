# How-to: Spreadsheet to CSV to YAML (.yml) file
Much of the documentation below has been taken directly from the **[Field Guide](https://github.com/ruthtillman/yaml-generator-for-hathitrust/blob/master/field_guide.md)** for the **[yaml-generator-for-hathitrust](https://github.com/ruthtillman/yaml-generator-for-hathitrust)** repository, which is the source of the Python script used here. (Indicated by **YGfHT/FG** in the information below.) 

## Recording item information
### Create a copy of **[this template](https://docs.google.com/spreadsheets/d/1tXg4p4iouy6OBnflIgYaC_AVBDDvhF_pym7eYVc6RMc/edit?usp=sharing)**. Fill in required item information as detailed below.  
- By entering information for multiple items in successive rows, multiple YAML files may be generated at once.
- To prevent any alteration to date formats, etc., which would prevent processing, apply plain-text formatting to all cells in your data-entry spreadsheet.
- It is important to remember that anytime you enter a number in the spreadsheet to indicate a captured page image or images, you are entering the number(s) for an *image file* or set of *image files*, and *not* for pages in a book or document. 
- When entering image file numbers in the spreadsheet, exclude leading zeros and filename extensions. For example, to input "00000001.tif" in the FRONT_COVER column, enter "1".
- Column headings in ALL CAPS below (FRONT_COVER, COPYRIGHT, etc.) are HathiTrust page tags, and image file numbers input in these columns will be tagged as such. Page-tag explanations in the table below were taken directly from a HathiTrust-provided example YAML file which is available **[here](https://drive.google.com/file/d/0B0EHs5JWGUMLWjU2OHVhQzN5WEk/view)** (this material is indicated with **HTEYF** in the information below).  The example YAML file, in turn, is linked to from the [HathiTrust Cloud Validation and Packaging Service document](https://docs.google.com/document/d/1OQ0SKAiOH8Xi0HVVxg4TryBrPUPtdv4qA70d8ghRltU/edit?usp=sharing).
- Quotation marks are used below to indicate specific values for entry, but should *not* be entered in the spreadsheet.
- **And an important note from [YGfHT/FG](https://github.com/ruthtillman/yaml-generator-for-hathitrust/blob/master/field_guide.md#how-to-input-information):** "Do NOT skip a question by pressing 'Enter'/'Return.' This may break the script. Instead, input N for Y/N questions and 0 for anything else." 

### Example files
- An example data-entry spreadsheet complete with input values is available **[here](https://docs.google.com/spreadsheets/d/1ixc8uVCmZAgtEU8S446XntZoeRVsCPcLSX_R-KnLD_4/edit?usp=sharing)**.
- Example output YAML files--both generated from the sample spreadsheet above--are available **[here](https://drive.google.com/a/uw.edu/file/d/1XL9BSejpJKPZbwVYZAmtgE4CiJe2pRmT/view?usp=sharing)** and **[here](https://drive.google.com/a/uw.edu/file/d/1MNK9B0tXiLXbOJW8AZ6pKKT5b-7uj5NY/view?usp=sharing)**. Note that YAML files output by the script will have the file extension ".yml", not "_YAML.txt" as in these sample files.    
  
  
  
| Column Heading | Input Instructions |
| --- | --- |
| Item barcode | Enter the UW-assigned item barcode (beginning 393520...) for the digitized item. In this context, an "item" may be defined as a book, document, set of documents, etc. having a single assigned barcode. |
| Scan Date YYYY-MM-DD | Enter the date (the first date, if more than one) of digital capture of the item. Be sure to enter this in the format given in the column heading. This date can be taken from the "date created" value shown for the first captured image file of a given item. |
| Scan Time HH:MM | Enter the start time of digital capture here. Be sure to enter this as shown in the column heading. This value can be taken from the "date created" value shown for the first captured image file of a given item. |
| Scan DST: Y/N | If the item was captured during daylight savings time enter "Y", if not enter "N". |
| "Y" if using BookDrive / If not, enter scanner maker | Entering "Y" will output the value "Atiz" in the "scanner_make" line of the output YAML file. If you are not using the Atiz BookDrive for capture, enter the manufacturer of the scanner or other digital capture device you are using. (Example: "Epson") |
| "Y" if using BookDrive / If not, enter scanner model | Entering "Y" will output the value "BookDrive Mark II" in the "scanner_model" line of the output YAML file. If you are not using the Atiz BookDrive for capture, enter the model of the scanner or other digital capture device you are using. (Example: "Expression 12000XL") |
| Bitone DPI | If the item was captured in black-and-white (bitone), enter the capture DPI value. If the item was captured in greyscale or color, enter zero. (Example: "400") |
| Contone DPI | If the item was captured in color or greyscale (contone), enter the capture DPI value here. If the item was captured in black-and-white (bitone), enter zero. (Example: "400") |
| Compression Date YYYY-MM-DD | Enter "N" if captured images are uncompressed. |
| Compression Time HH:MM | Enter "N" if captured images are uncompressed. |
| Compression DST: Y/N | Enter "N" if captured images are uncompressed. |
| Compression Tool(s) | Enter "N" if captured images are uncompressed. |
| Scanning Order ("Y"=L->R)) | Enter "Y" for books that were scanned from left to right. **See [note](https://github.com/ries07uw/HathiTrustYAMLgenerator/blob/master/HowTo.md#note) below.**|
| Reading Order ("Y"=L->R) | Enter "Y" for books that should be read from left to right. **See [note](https://github.com/ries07uw/HathiTrustYAMLgenerator/blob/master/HowTo.md#note) below.** |
| Filename extension | Enter the filename extension of the image files. All files should have the same format, so there should be one entry here. (Example: "tif") |
| Total number of images | Enter the total number of image files included in the item folder to be uploaded. |
| FRONT_COVER | [HTEYF](https://drive.google.com/file/d/0B0EHs5JWGUMLWjU2OHVhQzN5WEk/view): "Image of the front cover (if the cover of the book was scanned)" |
| TITLE_PARTS | [HTEYF](https://drive.google.com/file/d/0B0EHs5JWGUMLWjU2OHVhQzN5WEk/view): "Half title page (a sort of preliminary title page before the real one)" |
| TITLE | [HTEYF](https://drive.google.com/file/d/0B0EHs5JWGUMLWjU2OHVhQzN5WEk/view): "Title page recto (the front of the real title page)" |
| COPYRIGHT | [HTEYF](https://drive.google.com/file/d/0B0EHs5JWGUMLWjU2OHVhQzN5WEk/view): "Title page verso (the back of the real title page)" UW Note: ONLY use this if there is actually a copyright notice on the title page verso|
| TABLE_OF_CONTENTS | [HTEYF](https://drive.google.com/file/d/0B0EHs5JWGUMLWjU2OHVhQzN5WEk/view): "First page of the table of contents" |
| Roman Numeral Start | [YGfHT/FG](https://github.com/ruthtillman/yaml-generator-for-hathitrust/blob/master/field_guide.md#information-about-pages-and-pagination): "List the file number on which any Roman numerals start: Input the file number on which page ''" occurs. If the first Roman page is unnumbered, the user should still designate the file which should be 'i' and manually remove the labels if desired. Outputs orderlabel: 'i' and starts numbering." |
| End Roman Numerals | [YGfHT/FG](https://github.com/ruthtillman/yaml-generator-for-hathitrust/blob/master/field_guide.md#information-about-pages-and-pagination): "List the file number on which any Roman numerals end: Input the file number on which the final page with a Roman numeral occurs. The script uses it as a cap for pagination. Handles where the final orderlabel with a Roman numeral occurs. Roman numerals iterate through this." |
| PREFACE | [HTEYF](https://drive.google.com/file/d/0B0EHs5JWGUMLWjU2OHVhQzN5WEk/view): "First page of each section that appears between the title page verso and the first regularly numbered page. For example, a one-page dedication on page xvi would get this tag, and then the first page of a three-page preface starting on page xviii would also get this.  However, if the introduction of the text starts on page 1 (or on an unnumbered page followed by page 2), do not use this tag. Use for components occurring before and after the table of contents." |
| Page 1 | Note that only one entry is allowed here, even for items using the MULTIWORK_BOUNDARY tag described below. [YGfHT/FG](https://github.com/ruthtillman/yaml-generator-for-hathitrust/blob/master/field_guide.md#information-about-pages-and-pagination): "What is the file number on which page 1 occurs? Input the file number of page 1. Outputs orderlabel: '1' and starts page numbering." |
| FIRST_CONTENT_CHAPTER_START | [HTEYF](https://drive.google.com/file/d/0B0EHs5JWGUMLWjU2OHVhQzN5WEk/view): "First page of the first chapter with regular page numbering. If the first chapter with regular numbering is called the introduction, that's okay." |
| CHAPTER_PAGE | [HTEYF](https://drive.google.com/file/d/0B0EHs5JWGUMLWjU2OHVhQzN5WEk/view): "A sort of half title page for a chapter of grouping of chapters -- that is, a page that gives the name of the chapter or section that begins on the next page." |
| CHAPTER_START | [HTEYF](https://drive.google.com/file/d/0B0EHs5JWGUMLWjU2OHVhQzN5WEk/view): "Subsequent chapters with regular page numbering after the first. Also use this for the beginning of each appendix." |
| Final Page | [YGfHT/FG](https://github.com/ruthtillman/yaml-generator-for-hathitrust/blob/master/field_guide.md#information-about-pages-and-pagination): "What is the file number on which the final NUMBERED page occurs? Input the file number of the final page. Don't worry about listing the page number, the program will handle it. Determines when to stop the incremental loop that generates order labels." |
| BLANK | [HTEYF](https://drive.google.com/file/d/0B0EHs5JWGUMLWjU2OHVhQzN5WEk/view): "An intentionally blank page." |
| Unpaginated | [YGfHT/FG](https://github.com/ruthtillman/yaml-generator-for-hathitrust/blob/master/field_guide.md#information-about-pages-and-pagination): "List the file numbers of any pages outside the pagination sequence (not unpaginated but entirely skipped, such as photographic inserts): List ALL file numbers, comma-separated, which occur outside the pagination. This is not for pages which simply don't have visible page numbers. Some pages, even photographic inserts, will skip visible pagination but still occur within the general page sequence (e.g. 4 pages of photographs preceded by 32 and followed by 37). This is for cases where pages within the book occur entirely without pagination, e.g. page 32, 4 pages of pictures, followed by page 33. All file numbers must be input here as a list, not just the first and last of a sequence. In a case such as above, assuming page 32 starts on file 44, the user would input: 45, 46, 47, 48. The script can handle multiple instances of pagination breaks." |
| IMAGE_ON_PAGE | [HTEYF](https://drive.google.com/file/d/0B0EHs5JWGUMLWjU2OHVhQzN5WEk/view): "Use for plates (pages with only images, which often do not contain the regular page numbering)" |
| FOLDOUT | [HTEYF](https://drive.google.com/file/d/0B0EHs5JWGUMLWjU2OHVhQzN5WEk/view): "A page that folded out of the print original" |
| INDEX | [HTEYF](https://drive.google.com/file/d/0B0EHs5JWGUMLWjU2OHVhQzN5WEk/view): "The first page in a sequence containing an index" |
| REFERENCES | [HTEYF](https://drive.google.com/file/d/0B0EHs5JWGUMLWjU2OHVhQzN5WEk/view): "The first page in a sequence containing endnotes or a bibliography" |
| MULTIWORK_BOUNDARY | [HTEYF](https://drive.google.com/file/d/0B0EHs5JWGUMLWjU2OHVhQzN5WEk/view): "[F]or items with multiple volumes bound together" |
| BACK_COVER | [HTEYF](https://drive.google.com/file/d/0B0EHs5JWGUMLWjU2OHVhQzN5WEk/view): "Image of the back cover" |
  
## Generating a YAML file for upload
- Download the sheet with input values in CSV format.
- To prevent any alteration to date formats, etc., which would prevent processing, open the downloaded CSV file in a simple text-editing program such as [Notepad++](https://notepad-plus-plus.org/).
- Delete column headers--all content coming before the first digit of the first item's barcode--from the CSV file, and save changes. 
- Open the [Python script](MODIFIED_yaml_csv.py).
- Input the filepath, including filename, of the saved CSV file.
- Input the filepath where output YAML files should be saved.
- Confirm generated YAML file output.
- If images are uncompressed, the *image_compression_date*, *image_compression_agent*, and *image_compression_tool* lines should be deleted from output YAML files prior to HathiTrust upload. (See [notes regarding ideas for improvements](IdeasForImprovements.md).)

### Note:  
- [YGfHT/FG](https://github.com/ruthtillman/yaml-generator-for-hathitrust/blob/master/field_guide.md#information-about-scanning): "While HathiTrust can handle books where the last page or back cover is 00000001, this YAML output tool can only handle 'normal' English reading order if books were scanned in the same direction as they should be read. i.e. if they should be read right-to-left, then it can handle a right-to-left scan, but it can't handle a book read left-to-right but scanned right-to-left."

#### Next: [Ideas for future improvements](IdeasForImprovements.md)
