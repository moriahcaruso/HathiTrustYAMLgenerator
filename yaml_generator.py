import re, os

# A function that handles all the defaults and input for scanning information:
def scanningAndScannerInfo(f):
	global captureDate, scannerMake, scannerModel, scannerUser, bitoneRes, contoneRes, scanningOrder, readingOrder, imageCompressionAgent, imageCompressionDate, imageCompressionTool, imageCompressionToolList
	if DST.lower() == 'yes' or DST.lower() == 'y':
		DSTOffset = '6'
	else:
		DSTOffset = '5'
	captureDate = 'capture_date: ' + scanYearMonthDay + 'T' + scanTime + ':00-0' + DSTOffset + ':00\n'
	# SPECIFIC TO NOTRE DAME
	if scannerMakeInput.lower() == 'yes' or scannerMakeInput.lower() == 'y':
		scannerMake = 'scanner_make: Kirtas\n'
	else:
		scannerMake = 'scanner_make: ' + scannerMakeInput + '\n'
	if scannerModelInput.lower() == 'yes' or scannerModelInput.lower() == 'y':
		scannerModel = 'scanner_model: APT 1200\n'
	else:
		scannerModel = 'scanner_model: ' + scannerModelInput + '\n'
	# SPECIFIC TO NOTRE DAME
	scannerUser = 'scanner_user: "Notre Dame Hesburgh Libraries: Digital Production Unit"\n'
	if bitoneResInput != '0':
		bitoneRes = 'bitonal_resolution_dpi: ' + bitoneResInput + '\n'
	else:
		bitoneRes = ''
	if contoneResInput != '0':
		contoneRes = 'contone_resolution_dpi: ' + contoneResInput + '\n'
	else:
		contoneRes = ''
	if imageCompression.lower() == 'yes' or imageCompression.lower() == 'y':
		# SPECIFIC TO NOTRE DAME
		imageCompressionAgent = 'image_compression_agent: notredame\n'
		if compressionDST.lower() == 'yes' or compressionDST.lower() == 'y':
			compressionDSTOffset = '6'
		else:
			compressionDSTOffset = '5'
		imageCompressionDate = 'image_compression_date: ' + imageCompressionYearMonthDay + 'T' + imageCompressionTime + ':00-0' + compressionDSTOffset + ':00\n'
		if "," in imageCompressionToolList:
		    splitList = imageCompressionToolList.split(", ")
		    imageCompressionToolList = ''
		    for tool in splitList:
		        if tool == splitList[-1]:
		            imageCompressionToolList += '"' + tool + '"'
		        else:
		            imageCompressionToolList += '"' + tool + '", '
		else:
		    imageCompressionToolList = '"' + imageCompressionToolList + '"'
		imageCompressionTool = 'image_compression_tool: [' + imageCompressionToolList + ']\n'
	if scanningOrderInput.lower() == 'yes' or scanningOrderInput.lower() == 'y':
		scanningOrder = 'scanning_order: left-to-right\n'
	elif scanningOrderInput.lower() == 'no' or scanningOrderInput.lower() == 'n':
		scanningOrder = 'scanning_order: right-to-left\n'
	else:
		scanningOrder = 'scanning_order: left-to-right\n' #because let's be honest this is the most likely
	if readingOrderInput.lower() == 'yes' or readingOrderInput.lower() == 'y':
		readingOrder = 'reading_order: left-to-right\n'
	elif readingOrderInput.lower() == 'no' or readingOrderInput.lower() == 'n':
		readingOrder = 'reading_order: right-to-left\n'
	else:
		readingOrder = 'reading_order: left-to-right\n' #because let's be honest this is the most likely
	f.write(captureDate)
	f.write(scannerMake)
	f.write(scannerModel)
	f.write(scannerUser)
	if bitoneRes != '':
		f.write(bitoneRes)
	if contoneRes != '':
		f.write(contoneRes)
	if imageCompression.lower() == 'yes' or imageCompression.lower() == 'y':
		f.write(imageCompressionDate)
		f.write(imageCompressionAgent)
		f.write(imageCompressionTool)
	f.write(scanningOrder)
	f.write(readingOrder)

# Determines the length of the 000s to ensure that the filename is 8 characters.
def determinePrefixLength(fileNum):
	global prefixZeroes
	if 0 < fileNum < 10:
		prefixZeroes = '0000000'
	elif 10 <= fileNum < 100:
		prefixZeroes = '000000'
	elif 100 <= fileNum < 1000:
		prefixZeroes = '00000'
	elif 1000 <= fileNum < 10000:
		prefixZeroes = '0000'
	else:
		prefixZeroes = 'error'

# Creates the file's name. Combines the leading 0s, integer as string, and filetype, and outputs global variable fileName
def generateFileName(prefix, suffix, fileType):
	global fileName
	fileName = prefix + str(suffix) + '.' + fileType.lower()

# Uses the number of the reading start page to determine where the reading order starts/create orderLabel variable to be returned later.
# Handles and incrementations for orderNum and romanInt
def generateOrderLabel(fileNum):
	global readingStartNum, readingEndNum, orderNum, orderLabel, romanCap, romanInt, romanStart
	if fileNum == readingStartNum:
		orderNum = 1
	if fileNum == romanStart:
		romanInt = 1
	orderLabel = ''
	if romanCap != 0:
		if romanStart <= fileNum <= romanCap:
			orderLabel = 'orderlabel: "' + toRoman(romanInt) + '"'
			romanInt += 1
		elif romanCap < romanInt:
			orderLabel = ''
	if readingStartNum <= fileNum <= readingEndNum and fileNum not in unpaginatedPages:
		orderLabel = 'orderlabel: "' + str(orderNum) + '"'
		orderNum += 1

# If this is a Multiwork item (note, does not function right if no multiwork boundary input), casts the numbers to start/end lists, then defines start/end numbers. Lots of globals because they'll need to be manipulated more elsewhere.
def defineMultiWorkLists():
	global readingStartNum, readingEndNum, multiworkStartList, multiworkEndList, romanStartList, romanEndList, romanStart, romanCap
	multiworkStartList = list(readingStartNum)
	multiworkEndList = list(readingEndNum)
	readingStartNum = multiworkStartList[0]
	readingEndNum = multiworkEndList[0]
	if type(romanStart).__name__ != 'int':
		romanStartList = list(romanStart)
		romanEndList = list(romanCap)
		romanStart = romanStartList[0]
		romanCap = romanEndList[0]
	if type(romanStart).__name__ != 'int':
		romanStart = romanStart
		romanCap = romanCap

# Handles Start/End lists, pops off the first (0) number in the list, then resets start/end numbers. Again using globals because they'll need to be manipulated elsewhere.
def defineMultiworkCycle(fileNum):
	global readingStartNum, readingEndNum, multiworkStartList, multiworkEndList, orderNum, romanStartList, romanEndList, romanStart, romanCap, romanInt
	if fileNum in multiworkEndList:
		if fileNum != multiworkEndList[-1]:
			multiworkStartList.pop(0)
			readingStartNum = multiworkStartList[0]
			multiworkEndList.pop(0)
			readingEndNum = multiworkEndList[0]
	if fileNum in romanEndList:
		if fileNum != romanEndList[-1]:
			romanStartList.pop(0)
			romanStart = romanStartList[0]
			romanEndList.pop(0)
			romanCap = romanEndList[0]

# Adds conversion support to/from Roman numerals, taken from diveintopython.net examples
romanNumeralMap = (('m',  1000),
				('cm', 900),
				('d',  500),
				('cd', 400),
				('c',  100),
				('xc', 90),
				('l',  50),
				('xl', 40),
				('x',  10),
				('ix', 9),
				('v',  5),
				('iv', 4),
				('i',  1))

def toRoman(n):
	result = ''
	for numeral, integer in romanNumeralMap:
		while n >= integer:
			result += numeral
			n -= integer
	return result

def fromRoman(s):
	result = 0
	index = 0
	for numeral, integer in romanNumeralMap:
		while s[index:index+len(numeral)] == numeral:
			result += integer
			index += len(numeral)
	return result

# Processes inputs for various page numbers. Casts everything but covers, because there should only be one, into lists if they're not already lists. Could almost definitely be improved.
def inputToLists():
	global blankPages, chapterPages, chapterStart, copyrightPages, firstChapterStart, foldoutPages, imagePages, indexStart, multiworkBoundaries, prefacePages, referenceStartPages, tableOfContentsStarts, titlePages, halfTitlePages, unpaginatedPages
	if type(blankPages).__name__ == 'int':
		blankPages = [blankPages]
	if type(chapterPages).__name__ == 'int':
		chapterPages = [chapterPages]
	if type(chapterStart).__name__ == 'int':
		chapterStart = [chapterStart]
	if type(copyrightPages).__name__ == 'int':
		copyrightPages = [copyrightPages]
	if type(firstChapterStart).__name__ == 'int':
		firstChapterStart = [firstChapterStart]
	if type(foldoutPages).__name__ == 'int':
		foldoutPages = [foldoutPages]
	if type(imagePages).__name__ == 'int':
		imagePages = [imagePages]
	if type(indexStart).__name__ == 'int':
		indexStart = [indexStart]
	if type(multiworkBoundaries).__name__ == 'int':
		multiworkBoundaries = [multiworkBoundaries]
	if type(prefacePages).__name__ == 'int':
		prefacePages = [prefacePages]
	if type(unpaginatedPages).__name__ == 'int':
		unpaginatedPages = [unpaginatedPages]
	if type(referenceStartPages).__name__ == 'int':
		referenceStartPages = [referenceStartPages]
	if type(tableOfContentsStarts).__name__ == 'int':
		tableOfContentsStarts = [tableOfContentsStarts]
	if type(titlePages).__name__ == 'int':
		titlePages = [titlePages]
	if type(halfTitlePages).__name__ == 'int':
		halfTitlePages = [halfTitlePages]

# Handles the reading labels. Uses list function which then gets split apart, so that multiple labels can apply to same page if relevant.
def generateLabel(fileNum):
	global label
	labelList = []
# Testing whether or not a page has a label
	if fileNum == frontCover:
		labelList.append('"FRONT_COVER"')
	if fileNum == backCover:
		labelList.append('"BACK_COVER"')
	if fileNum in blankPages:
		labelList.append('"BLANK"')
	if fileNum in chapterPages:
		labelList.append('"CHAPTER_PAGE"')
	if fileNum in chapterStart:
		labelList.append('"CHAPTER_START"')
	if fileNum in copyrightPages:
		labelList.append('"COPYRIGHT"')
	if fileNum in firstChapterStart:
		labelList.append('"FIRST_CONTENT_CHAPTER_START"')
	if fileNum in foldoutPages:
		labelList.append('"FOLDOUT"')
	if fileNum in imagePages:
		labelList.append('"IMAGE_ON_PAGE"')
	if fileNum in indexStart:
		labelList.append('"INDEX"')
	if fileNum in multiworkBoundaries:
		labelList.append('"MULTIWORK_BOUNDARY"')
	if fileNum in prefacePages:
		labelList.append('"PREFACE"')
	if fileNum in referenceStartPages:
		labelList.append('"REFERENCES"')
	if fileNum in tableOfContentsStarts:
		labelList.append('"TABLE_OF_CONTENTS"')
	if fileNum in titlePages:
		labelList.append('"TITLE"')
	if fileNum in halfTitlePages:
		labelList.append('"TITLE_PARTS"')
	if not labelList:
		label = ''
	else:
		label = 'label: ' + ', '.join(labelList)

# Combines all functions to write the file.
def writeFile(finalNumber, readingStartNum, readingEndNum, fileType, outputFile, romanCap, workingDir):
	global orderNum, multiworkEndList, romanEndList, romanInt
	originalDir = os.getcwd()
	os.chdir(workingDir)
	f = open(outputFile, 'w')
	scanningAndScannerInfo(f)
	f.write('pagedata:\n')
	fileNum = 1
	orderNum = 1
	romanInt = 1
	multiworkEndList = [0]
	romanEndList = [0]
	if multiworkBoundaries != 0:
		defineMultiWorkLists()
	inputToLists()
	while fileNum <= finalNumber:
		determinePrefixLength(fileNum)
		generateFileName(prefixZeroes, fileNum, fileType)
		generateOrderLabel(fileNum)
		if multiworkBoundaries != 0:
			defineMultiworkCycle(fileNum)
		generateLabel(fileNum)
		comma = ''
		if orderLabel != '' and label !='':
			comma = ', '
		output = '    ' + fileName + ': { ' + orderLabel + comma + label + ' }\n'
		f.write(output)
		fileNum += 1
	f.close()
	print "File " + outputFile + " created in " + workingDir
	os.chdir(originalDir)

# Putting input into a function vs. having a huge list of inputs at the end.
def gatherInput():
	global fileType, workingDir, finalNumber, readingStartNum, readingEndNum, frontCover, outputFile, backCover, blankPages, chapterPages, chapterStart, copyrightPages, firstChapterStart, foldoutPages, imagePages, indexStart, multiworkBoundaries, prefacePages, referenceStartPages, tableOfContentsStarts, titlePages, halfTitlePages, romanStart, romanCap, scanYearMonthDay, scanTime, DST, scannerModelInput, scannerMakeInput, bitoneResInput, contoneResInput, compressionDST, imageCompression, imageCompressionTime, imageCompressionTool, imageCompressionYearMonthDay, imageCompressionTime, imageCompressionAgent, imageCompressionToolList, scanningOrderInput, readingOrderInput, unpaginatedPages
	print 'INSTRUCTIONS:\n1. When listing multiple numbers, separate with a comma and space, e.g. "1, 34"\n\n2. Some entries such as first chapter should only have multiple entries if multiple works are bound together, such as two journal volumes.\n\n3. When a question doesn\'t apply and isn\'t Y/N, ENTER 0. Not entering anything will confuse the program.\n\n4. Do not use quotation marks.\n'
	workingDir = raw_input("Input the directory in which the finished file should be placed: ")
	outputFile = raw_input("Name of the file to be created or overwritten (Include extension, e.g. meta.yml): ")
	print 'The following sequence of questions have to do with the scanning itself.\n'
	scanYearMonthDay = raw_input("What is the date of the scan, formatted as YYYY-MM-DD, e.g. 2015-04-01? ")
	while not re.match('(19|20|21)\d{2}\-(0[1-9]|1[0-2])\-(0[1-9]|1\d|2\d|3[0-1])', scanYearMonthDay) :
	    print 'The date was invalid. Please use the YYYY-MM-DD format.'
	    scanYearMonthDay = raw_input("What is the date of the scan, formatted as YYYY-MM-DD, e.g. 2015-04-01? ")
	scanTime = raw_input("What was the time of the scan in 24-hour time, e.g. 09:30 or 15:45? ")
	while not re.match('(0\d|1\d|2[0-4])\:([0-5]\d)', scanTime) :
	    print 'The time was invalid, please input as 24-hour time, e.g. 07:15 or 20:21.'
	    scanTime = raw_input("What was the time of the scan in 24-hour time, e.g. 09:30 or 15:45? ")
	DST = raw_input("Was it daylight savings time: Y/N? ")
	scannerMakeInput = raw_input("If this was scanned on the Kirtas, enter 'YES' or 'Y'. Otherwise enter the name of the scanner make (e.g. Bookeye): ")
	scannerModelInput = raw_input("If this was scanned on the Kirtas, enter 'YES' or 'Y'. Otherwise enter the name of the scanner model (e.g. 4 V1A): ")
	bitoneResInput = raw_input("What is the dpi resolution of bitone, b&w, images (input just numbers, e.g. 600)? Or enter '0' if none exist: ")
	while not re.match('(0|\d{3}|\d{4})', bitoneResInput):
		print "The number you entered was not three or four digits. Please re-input as 300 or 600 or 1000, etc.  Or enter '0' if none exist:"
		bitoneResInput = raw_input("What is the dpi resolution of bitone, b&w, images (input just numbers, e.g. 600)? Or enter '0' if none exist: ")
	contoneResInput = raw_input("What is the dpi resolution of contone, grayscale or color, images (input just numbers, e.g. 400)? Or enter '0' if none exist: ")
	while not re.match('(0|\d{3}|\d{4})', contoneResInput):
		print "The number you entered was not three or four digits. Please re-input as 300 or 600 or 1000, etc. Or enter '0' if none exist: "
		contoneResInput = raw_input("What is the dpi resolution of contone, grayscale or color, images (input just numbers, e.g. 400)? Or enter '0' if none exist: ")
	imageCompression = raw_input("If any of the images are compressed, enter 'YES' or 'Y': ")
	if imageCompression.lower() == 'yes' or imageCompression.lower() == 'y':
		imageCompressionYearMonthDay = raw_input("What is the date of the compression, formatted as YYYY-MM-DD, e.g. 2015-04-01? ")
		while not re.match('(19|20|21)\d{2}\-(0[1-9]|1[0-2])\-(0[1-9]|1\d|2\d|3[0-1])', imageCompressionYearMonthDay) :
		    print 'The date was invalid. Please use the YYYY-MM-DD format.'
		    imageCompressionYearMonthDay = raw_input("What is the date of the scan, formatted as YYYY-MM-DD, e.g. 2015-04-01? ")
		imageCompressionTime = raw_input("What was the time of the compression in 24-hour time, e.g. 09:30 or 15:45? ")
		while not re.match('(0\d|1\d|2[0-4])\:([0-5]\d)', imageCompressionTime) :
		    print 'The time was invalid, please input as 24-hour time, e.g. 07:15 or 20:21.'
		    imageCompressionTime = raw_input("What was the time of the scan in 24-hour time, e.g. 09:30 or 15:45? ")
		compressionDST = raw_input("Was compression done during daylight savings time: Y/N? ")
		imageCompressionToolList = raw_input("What tools were used to compress the images? Include versions. Separate with comma and space, e.g. kdu_compress v7.2.3, ImageMagick 6.7.8: ")
	scanningOrderInput = raw_input("Was the book scanned left-to-right (normal English reading order), Y/N? ")
	print "This section gathers information about the book's files and reading order."
	readingOrderInput = raw_input("Is the book READ left-to-right (normal English reading order), Y/N? ")
	fileType = raw_input("What is the filename extension of the images? ")
	finalNumber = input("What is the total number of image files? ")
	frontCover = input("What file number is the front cover? ")
	halfTitlePages = input("List the file numbers of any half title pages (preliminary title pages often before the first title page, little or no information on reverse): ")
	titlePages = input("List file number of any title pages (one per work): ")
	copyrightPages = input("List the file number of the title page verso (back of title page containing copyright info) for each work: ")
	tableOfContentsStarts = input("List file numbers of the first page of any Table of Contents: ")
	romanStart = input("List the file number on which any Roman numerals start: ")
	romanCap = input("List the file number on which any Roman numerals end: " )
	prefacePages = input("List the file number of each Preface, defined as sections that appear between the title page verso/copyright and page 1. Do not list any Prefaces beginning on or after page 1: ")
	readingStartNum = input("What is the file number on which page 1 occurs? ")
	firstChapterStart = input("List the file number of the first chapter on a regularly-numbered page (may be Preface) for each work: ")
	chapterPages = input("List the file numbers of pages containing only chapter names: ")
	chapterStart = input("List file numbers of the start of each chapter **EXCEPT** the first, including appendices: ")
	readingEndNum = input("What is the file number on which the final NUMBERED page occurs? ")
	blankPages = input("List the file numbers of any blank pages: ")
	unpaginatedPages = input("List the file numbers of any pages outside the pagination sequence (not unpaginated but entirely skipped, such as photographic inserts): ")
	imagePages = input("List the file number of any page which is only an image: ")
	foldoutPages = input("List the file number of any page that is a scan of a foldout: ")
	indexStart = input("List the file number of any pages which are the FIRST page of an index: ")
	referenceStartPages = input("List the file number of the first page of any set of references or bibliography: ")
	multiworkBoundaries = input("List the file number of any multi-work boundaries: ")
	backCover = input("What is the file number of the back cover? ")

gatherInput()
writeFile(finalNumber, readingStartNum, readingEndNum, fileType, outputFile, romanCap, workingDir)
