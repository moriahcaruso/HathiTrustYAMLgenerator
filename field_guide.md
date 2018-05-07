# Field Guide: A guide to the input questions asked by the YAML Generator for HathiTrust Submissions

Since the problem uses the CLI vs. a GUI, there isn't a lot of space to explain what some of the requested inputs actually mean. This document is a guide to the questions asked, explaining what each will output in the final document. Information about what they should represent comes from HathiTrust's own YAML documentation as well.

## How to Input Information

- **Dates**. Always input dates in ISO-8601 format with dashes as YYYY-MM-DD. The date inputs will be combined with times entered to create a full timestamp.
- **Times**. Always input times in 24-hour format as HH:MM, 08:30 or 20:30 for 8:30 am/pm, for example. These will be combined with dates entered to create a full timestamp. Do not include :SS (seconds).
- **DST**. When asking for date/time information, the script also asks whether it was DST or not at the time (because programming it to automatically know that would take a great deal of time). This will toggle between offset -5 and offset -6, as the institution using the script is in the Eastern time zone. Those hardcoded numbers can be changed in the script itself to fit other regions.
- **File numbers**. Input file numbers numbers of the filename without any leading 0s (e.g. 5 for 00000005.jp2 or 215 for 00000215.tif) although leading 0s do not break the program. Everything except front and back cover allows for multiple file numbers to be separated with a ", " and does not require them to be in order. Do not use quotation marks or final periods after entering file numbers. Example: 1, 35, 4, 29
- **Null information**. Do **NOT** skip a question by pressing "Enter"/"Return." This may break the script. Instead, input N for Y/N questions and 0 for anything else. Questions about scanner make/model are Y/INPUT questions, see more about them under **Information About Scanning**.

**Do Not Input**

- Quotation marks
- Extra commas
- Page numbers. *Always* input the FILE number.

## Output File

- **Input the directory in which the finished file should be placed:** Input the full directory path to wherever the file should be written (or overwritten). Uses python's os function to change directories while working, though for completeness' sake, it changes back to the current one as a part of wrapping up.
- **Name of the file to be created or overwritten (Include extension, e.g. meta.yml):** designates the output file, in the same directory as the Python script. If the file doesn't exist, it will be created. If it exists, this program will **overwrite** it, so exercise caution. It should end in .yml although the script will generate .txt/.xml/etc. but it will be formatted as YAML. Example input: meta.yml

## Information About Scanning

This section gathers information about the scanning process itself. If the files have been compressed, you have the option of recording information about that as well with a Y/N toggle.

- **What is the date of the scan, formatted as YYYY-MM-DD, e.g. 2015-04-01?** Gathers the scan date to be turned into a timestamp. Will run tests to ensure it complies with ISO-8601 format and prompt you to re-enter if a date is invalid. Tester is mildly flawed, as will accept DD up to 31 without limiting months which only have 28-30 days. Outputs part of `capture_date`.
- **What was the time of the scan in 24-hour time, e.g. 09:30 or 15:45?** Gathers the scan time to be combined and turned into a timestamp. Will run basic tests to ensure it's a 24-hour time. Only accepts HH:MM, no AM/PM. Do not include :SS (seconds). Outputs part of `capture_date`.
- **Was it daylight savings time: Y/N?** Handles a switch to output the offset from UTC, either -5 or -6. See README.md -> **Personalizing the YAML Generator to Your Repository** for information about changing this switch. Outputs part of `capture_date`.
- **If this was scanned on the Kirtas, enter 'YES' or 'Y'. Otherwise enter the name of the scanner make (e.g. Bookeye):** The creating institution uses a Kirtas scanner. If you also use a Kirtas, enter Y. If you use another scanner make, input just the name of the MAKE (e.g. Bookeye). Outputs `scanner_make`.
- **If this was scanned on the Kirtas, enter 'YES' or 'Y'. Otherwise enter the name of the scanner model (e.g. 4 V1A):** The creating institution's scanner model is an APT 1200. If you use a Kirtas APT 1200, press Y here. Otherwise input the model info of your scanner (e.g. APT 2400). Outputs `scanner_model`.
- **What is the dpi resolution of bitone, b&w, images (input just numbers, e.g. 600)? Or enter '0' if none exist:** If submitting any bitone (black & white, normally TIFF) images, input the DPI of those images. Only input numbers. Outputs `bitonal_resolution_dpi`.
- **What is the dpi resolution of contone, grayscale or color, images (input just numbers, e.g. 400)? Or enter '0' if none exist:** If submitting any continuous tone (contone) images (grayscale or color, normally JP2 but HathiTrust will convert contone TIFF), input the DP of those images. Only input numbers. Outputs `contone_resolution_dpi`.
- **If any of the images are compressed, enter 'YES' or 'Y':** Entering Yes or Y here triggers a set of questions about compression. Entering N or No allows one to skip those questions if they don't apply. Does not output to a specific field.
- **What is the date of the compression, formatted as YYYY-MM-DD, e.g. 2015-04-01?** As above, gathers date of compression to turn into a timestamp. As above, validates format and won't accept non-ISO-compliant dates. Outputs part of `image_compression_date`.
- **What was the time of the compression in 24-hour time, e.g. 09:30 or 15:45?** As above, gathers time of compression to turn into a timestamp. As above, validates format and won't accept non-HH:MM input. Outputs part of `image_compression_date`.
- **Was compression done during daylight savings time: Y/N?** Handles a switch to output the offset from UTC, either -5 or -6. See README.md -> **Personalizing the YAML Generator to Your Repository** for information about changing this switch. Outputs part of `image_compression_date`.
- **What tools were used to compress the images? Include versions. Separate with comma and space, e.g. kdu_compress v7.2.3, ImageMagick 6.7.8:** HathiTrust would like information about what software tools were used to compress the images. This can handle multiple software types, just use a comma and space to separate them. Spaces and periods are fine in the name and version of the software. Outputs `image_compression_tool`.
- **Was the book scanned left-to-right (normal English reading order), Y/N?** Input the direction in which the book was scanned. Note issues in reading order below. Outputs `scanning_order`.
- **Is the book READ left-to-right (normal English reading order), Y/N?** Input the direction in which the book should be **read** (Y for "normal" English). **Important Note:** While HathiTrust can handle books where the last page or back cover is 00000001, this YAML output tool can only handle "normal" English reading order if books were scanned in the same direction as they should be read. i.e. if they should be read right-to-left, then it can handle a right-to-left scan, but it can't handle a book read left-to-right but scanned right-to-left. However, even in these cases, it can still be used to generate a list of images and attach label data to them. If the book is right-to-left, enter 0 for page 1 and final page designations. Outputs `reading_order`.

Fields hardcoded into the YAML generator because they're universal for our institution:

- `scanner_user`
- `image_compression_agent`

## Information About Files

This section gathers some basic information about the files themselves:

- **What is the filename extension of the images?** Input the extension of the images as lowercase, e.g. "tif" or "jp2." This handles the ending of the list of files, determining whether it should be 00000001.tif or 00000001.jp2.
- **What is the total number of image files?** Input the total number of image files. The script generates a list of images, starting with 00000001 and ending with the number input here. Example: 215 (and filetype TIFF). Files listed will be 00000001.tif to 00000215.tif.

## Information About Pages and Pagination

This section gathers information about the actual pagination. Besides normal Arabic numerals, YAML generator can handle Roman numeral pagination at either the beginning or the end (or throughout the book, in which case enter 0 for both questions about non-Roman pagination).

- **List the file number on which any Roman numerals start:** Input the file number on which page "i" occurs. If the first Roman page is unnumbered, the user should still designate the file which **should** be "i" and manually remove the labels if desired. Outputs `orderlabel: "i"` and starts numbering.
- **List the file number on which any Roman numerals end:** Input the file number on which the final page with a Roman numeral occurs. The script uses it as a cap for pagination. Handles where the final `orderlabel` with a Roman numeral occurs. Roman numerals iterate through this.
- **What is the file number on which page 1 occurs?** Input the file number of page 1. Outputs `orderlabel: "1"` and starts page numbering.
- **What is the file number on which the final NUMBERED page occurs?** Input the file number of the final page. Don't worry about listing the page number, the program will handle it. Determines when to stop the incremental loop that generates order labels.
- **List the file numbers of any pages outside the pagination sequence (not unpaginated but entirely skipped, such as photographic inserts):** List ALL file numbers, comma-separated, which occur outside the pagination. This is **not** for pages which simply don't have visible page numbers. Some pages, even photographic inserts, will skip visible pagination but still occur within the general page sequence (e.g. 4 pages of photographs preceded by 32 and followed by 37). This is for cases where pages within the book occur entirely without pagination, e.g. page 32, 4 pages of pictures, followed by page 33. All file numbers must be input here as a list, not just the first and last of a sequence. In a case such as above, assuming page 32 starts on file 44, the user would input: `45, 46, 47, 48`. The script can handle multiple instances of pagination breaks.

What about multi-work issues?

Multi-work issue pagination is handled by the first 4 questions (everything but pages outside the pagination) and the much later question about multi-work boundaries. If the multi-work boundary question has at least one non-`0` number as an input, it triggers the tests for multiple starting and ending pagination numbers. The program will be confused starting/ending numbers are a list but multi-work boundary is `0` or if there's a non-`0` multi-work boundary with only a single start and end number.

## Information About Labels

HathiTrust allows one to label a variety of pages. None of these are necessarily required, though the institution may wish to decide which should be a standard part of their submissions (e.g. chapters) vs. which should be considered extra value (e.g. image pages). Each line explains which label will be added to the file number's description. e.g. 00000001.tiff: { label: "FRONT_COVER" }. For any field which doesn't exist within the book or for which no data exists, enter: `0`

- **What file number is the front cover?** Only accepts a single number, not a list of numbers. Outputs `label: "FRONT_COVER"`
- **List the file numbers of any half title pages (preliminary title pages often before the first title page, little or no information on reverse):** The half title page generally has a title, a blank reverse (verso) side, and occurs directly before the title page. Unlike title pages, it generally doesn't have any extra info about author, publisher, etc.. Not all books have half title pages. Outputs `label: "TITLE_PARTS"`
- **List file number of any title pages (one per work):** The actual title page. Outputs `label: "TITLE"`
- **List the file number of the title page verso (back of title page containing copyright info) for each work:** The back or "verso" side of the title page. Generally includes copyright information, information about publisher, LC or Dewey call number, etc. Outputs `label: "COPYRIGHT"`
- **List file numbers of the first page of any Table of Contents:** Any Table of Contents. Outputs. `label: "TABLE_OF_CONTENTS"`
- **List the file number of each Preface, defined as sections that appear between the title page verso/copyright and page 1. Do not list any Prefaces beginning on or after page 1:** This wordy because of how HathiTrust designates a "Preface." In HathiTrust's terms, a Preface may only appear before the book's Page 1 occurs. If anything **titled** "Preface" occurs after Page 1, treat it as the first chapter (see below). Outputs `label: "PREFACE"`
- **List the file number of the first chapter on a regularly-numbered page (may be Preface) for each work:** As above, HathiTrust considers the first chapter of the book the first chapter (including a Preface) to start after page 1. This is a very specific label used to designate where the first regular chapter starts and is handled separately from other chapters. Outputs `label: "FIRST_CONTENT_CHAPTER_START"`
- **List the file numbers of pages containing only chapter names:** Like half title pages, these are pages which occur before the start of a chapter which only contain the name of the chapter or perhaps the name and a short epitaph. Outputs `label: "CHAPTER_PAGE"`
- **List file numbers of the start of each chapter EXCEPT the first, including appendices:** A list of file numbers of where each chapter actually starts. Can be page with header if the contents of that chapter start on that page. Outputs `label: "CHAPTER_START"`
- **List the file numbers of any blank pages:** In order to ensure readers know that a page really should be blank, HathiTrust supports the labeling of blank pages, whether blank pages at the front and rear of the book or blank pages in the middle (following a chapter, for example). Outputs `label: "BLANK"`
- **List the file number of any page which is only an image:** A list of file numbers of files which represent pages with only an image or illustration (plate), not textual content. These may be pages outside the pagination sequence as described above, but a full-page image does not necessarily imply a lack of page number. Thus, reading order numbers will still be included unless the pages are also noted as outside the pagination sequence as well. Outputs `label: "IMAGE_ON_PAGE"`
- **List the file number of any page that is a scan of a foldout:** A list of file numbers of any pages which are scans of foldouts, either mid-book or at the end. As with pages which are only images, these foldouts may be outside the page numbering, but such information must be put into the list of file numbers of pages outside pagination sequence. Outputs `label: "FOLDOUT"`
- **List the file number of any pages which are the FIRST page of an index:** A list of file numbers of starts of any indexes. As with chapters, only the first page of the index should be labeled. Multiple indexes in a book is fine (e.g. a hymnal, which has title index and line-by-line index or a cookbook with multiple indexes). Outputs `label: "INDEX"`
- **List the file number of the first page of any set of references or bibliography:** A list of file numbers of starts of any reference sections OR bibliographies. As with chapters, only the first page should be labeled. Outputs `label: "REFERENCES"`
- **List the file number of any multi-work boundaries:** This label indicates the boundary between multiple items bound together (such as two volumes of a journal or serial publication). It is also necessary for pagination of multi-work items. Outputs `label "MULTIWORK_BOUNDARY"`
- **What is the file number of the back cover?** Only accepts a single number, not a list of numbers. Outputs `label: "BACK_COVER"`
