import re, os, csv

# A function that handles all the defaults and input for scanning information:
# DST offset changed from original code to Seattle time
def scanningAndScannerInfo(f):
	global captureDate, scannerMake, scannerModel, scannerUser, bitoneRes, contoneRes, scanningOrder, readingOrder, imageCompressionAgent, imageCompressionDate, imageCompressionTool, imageCompressionToolList
	if DST.lower() == 'yes' or DST.lower() == 'y':
		DSTOffset = '8'
	else:
		DSTOffset = '7'
	captureDate = 'capture_date: ' + scanYearMonthDay + 'T' + scanTime + ':00-0' + DSTOffset + ':00\n'
	# Default scanner values changed to BookDrive Mark II
	if scannerMakeInput.lower() == 'yes' or scannerMakeInput.lower() == 'y':
		scannerMake = 'scanner_make: Atiz\n'
	else:
		scannerMake = 'scanner_make: ' + scannerMakeInput + '\n'
	if scannerModelInput.lower() == 'yes' or scannerModelInput.lower() == 'y':
		scannerModel = 'scanner_model: BookDrive Mark II\n'
	else:
		scannerModel = 'scanner_model: ' + scannerModelInput + '\n'
	# Default scanner user changed to UWL PS
	scannerUser = 'scanner_user: "University of Washington"\n'
	if bitoneResInput != '0':
		bitoneRes = 'bitonal_resolution_dpi: ' + bitoneResInput + '\n'
	else:
		bitoneRes = ''
	if contoneResInput != '0':
		contoneRes = 'contone_resolution_dpi: ' + contoneResInput + '\n'
	else:
		contoneRes = ''
	if imageCompression.lower() == 'yes' or imageCompression.lower() == 'y':
		# Only the Agent has been changed, all other image compression defaults, etc., are as in original code
		# For further development--change script so that no compression info is put into YAML if no values are present
		imageCompressionAgent = 'image_compression_agent: universityofwashington\n'
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
	if fileNum == int(readingStartNum):
		orderNum = 1
	if fileNum == int(romanStart):
		romanInt = 1
	orderLabel = ''
	if int(romanCap) != 0:
		if int(romanStart) <= fileNum <= int(romanCap):
			orderLabel = 'orderlabel: "' + toRoman(romanInt) + '"'
			romanInt += 1
		elif int(romanCap) < romanInt:
			orderLabel = ''
	if int(readingStartNum) <= fileNum <= int(readingEndNum) and fileNum not in unpaginatedPages:
		orderLabel = 'orderlabel: "' + str(orderNum) + '"'
		orderNum += 1

# If this is a Multiwork item (note, does not function right if no multiwork boundary input), casts the numbers to start/end lists, then defines start/end numbers. Lots of globals because they'll need to be manipulated more elsewhere.
def defineMultiWorkLists():
	global readingStartNum, readingEndNum, multiworkStartList, multiworkEndList, romanStartList, romanEndList, romanStart, romanCap
	multiworkStartList = map(int, readingStartNum.split(", "))
	multiworkEndList = map(int, readingEndNum.split(", "))
	readingStartNum = multiworkStartList[0]
	readingEndNum = multiworkEndList[0]
	if ", " in romanStart:
		romanStartList = map(int, romanStart.split(", "))
		romanEndList = map(int, romanCap.split(", "))
		romanStart = romanStartList[0]
		romanCap = romanEndList[0]
#	if type(romanStart).__name__ != 'int':
#		romanStart = romanStart
#		romanCap = romanCap
# This section seemed duplicative? But we'll see? The "if" clause is wrong for the CSV verion though...so would have to make sure that's fixed if actually deploying.

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
# When coming from CSV, types are always now 'str'. So how

def inputToLists():
	global blankPages, chapterPages, chapterStart, copyrightPages, firstChapterStart, foldoutPages, imagePages, indexStart, multiworkBoundaries, prefacePages, referenceStartPages, tableOfContentsStarts, titlePages, halfTitlePages, unpaginatedPages
	if ", " in blankPages:
		 blankPages = map(int, blankPages.split(", "))
	else:
		blankPages = [int(blankPages)]
	if ", " in chapterPages:
		 chapterPages = map(int, chapterPages.split(", "))
	else:
		chapterPages = [int(chapterPages)]
	if ", " in chapterStart:
		 chapterStart = map(int, chapterStart.split(", "))
	else:
		chapterStart = [int(chapterStart)]
	if ", " in copyrightPages:
		 copyrightPages = map(int, copyrightPages.split(", "))
	else:
		copyrightPages = [int(copyrightPages)]
	if ", " in firstChapterStart:
		 firstChapterStart = map(int, firstChapterStart.split(", "))
	else:
		firstChapterStart = [int(firstChapterStart)]
	if ", " in foldoutPages:
		 foldoutPages = map(int, foldoutPages.split(", "))
	else:
		foldoutPages = [int(foldoutPages)]
	if ", " in imagePages:
		 imagePages = map(int, imagePages.split(", "))
	else:
		imagePages = [int(imagePages)]
	if ", " in indexStart:
		 indexStart = map(int, indexStart.split(", "))
	else:
		indexStart = [int(indexStart)]
	if ", " in multiworkBoundaries:
		 multiworkBoundaries = map(int, multiworkBoundaries.split(", "))
	else:
		multiworkBoundaries = [int(multiworkBoundaries)]
	if ", " in prefacePages:
		 prefacePages = map(int, prefacePages.split(", "))
	else:
		prefacePages = [int(prefacePages)]
	if ", " in unpaginatedPages:
		 unpaginatedPages = map(int, unpaginatedPages.split(", "))
	else:
		unpaginatedPages = [int(unpaginatedPages)]
	if ", " in referenceStartPages:
		 referenceStartPages = map(int, referenceStartPages.split(", "))
	else:
		referenceStartPages = [int(referenceStartPages)]
	if ", " in tableOfContentsStarts:
		 tableOfContentsStarts = map(int, tableOfContentsStarts.split(", "))
	else:
		tableOfContentsStarts = [int(tableOfContentsStarts)]
	if ", " in titlePages:
		 titlePages = map(int, titlePages.split(", "))
	else:
		titlePages = [int(titlePages)]
	if ", " in halfTitlePages:
		 halfTitlePages = map(int, halfTitlePages.split(", "))
	else:
		halfTitlePages = [int(halfTitlePages)]


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
def writeFile():
	global finalNumber, readingStartNum, readingEndNum, fileType, outputFile, romanCap, workingDir, orderNum, multiworkEndList, romanEndList, romanInt
	originalDir = os.getcwd()
	os.chdir(workingDir)
	outputFile = outputFile + '.yml'
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
	pathToFile = raw_input("Provide a link to the CSV file: ")
	workingDir = raw_input("Provide the directory in which the finished file should be placed: ")
	hathi_file = open(pathToFile)
	hathi_csv = csv.reader(hathi_file)
	for row in hathi_csv:
		if row[0] == '':
			outputFile = 'no_barcode'
		else:
			outputFile = row[0]
		if row[1] == '':
		    scanYearMonthDay = "0"
		else:
		    scanYearMonthDay = row[1]
		if row[2] == '':
		    scanTime = "0"
		else:
		    scanTime = row[2]
		if row[3] == '':
		    DST = "0"
		else:
		    DST = row[3]
		if row[6] == '':
		    bitoneResInput = "0"
		else:
		    bitoneResInput = row[6]
		if row[7] == '':
		    contoneResInput = "0"
		else:
		    contoneResInput = row[7]
		if row[12] == '':
		    scanningOrderInput = 'Y'
		else:
		    scanningOrderInput = row[12]
		if row[13] == '':
		    readingOrderInput = 'Y'
		else:
		    readingOrderInput = row[13]
		if row[15] == '':
		    finalNumber = 0
		else:
		    finalNumber = int(row[15])
		if row[16] == '':
		    frontCover = 0
		else:
		    frontCover = int(row[16])
		if row[17] == '':
		    halfTitlePages = "0"
		else:
		    halfTitlePages = row[17]
		if row[18] == '':
		    titlePages = "0"
		else:
		    titlePages = row[18]
		if row[19] == '':
		    copyrightPages = "0"
		else:
		    copyrightPages = row[19]
		if row[20] == '':
		    tableOfContentsStarts = "0"
		else:
		    tableOfContentsStarts = row[20]
		if row[21] == '':
		    romanStart = "0"
		else:
		    romanStart = row[21]
		if row[22] == '':
		    romanCap = "0"
		else:
		    romanCap = row[22]
		if row[23] == '':
		    prefacePages = "0"
		else:
		    prefacePages = row[23]
		if row[24] == '':
		    readingStartNum = "0"
		else:
		    readingStartNum = row[24]
		if row[25] == '':
		    firstChapterStart = "0"
		else:
		    firstChapterStart = row[25]
		if row[26] == '':
		    chapterPages = "0"
		else:
		    chapterPages = row[26]
		if row[27] == '':
		    chapterStart = "0"
		else:
		    chapterStart = row[27]
		if row[28] == '':
		    readingEndNum = "0"
		else:
		    readingEndNum = row[28]
		if row[29] == '':
		    blankPages = "0"
		else:
		    blankPages = row[29]
		if row[30] == '':
		    unpaginatedPages = "0"
		else:
		    unpaginatedPages = row[30]
		if row[31] == '':
		    imagePages = "0"
		else:
		    imagePages = row[31]
		if row[32] == '':
		    foldoutPages = "0"
		else:
		    foldoutPages = row[32]
		if row[33] == '':
		    indexStart = "0"
		else:
		    indexStart = row[33]
		if row[34] == '':
		    referenceStartPages = "0"
		else:
		    referenceStartPages = row[34]
		if row[35] == '':
		    multiworkBoundaries = "0"
		else:
		    multiworkBoundaries = row[35]
		if row[36] == '':
		    backCover = 0
		else:
		    backCover = int(row[36])
		if row[14] == '':
		    fileType = 'tif'
		else:
		    fileType = row[14]
		if row[4] == '':
		    scannerMakeInput = 'y'
		else:
		    scannerMakeInput = row[4]
		if row[5] == '':
		    scannerModelInput = 'y'
		else:
		    scannerModelInput = row[5]
		if row[8] == '':
		    imageCompression = 'n'
		else:
		    imageCompression = 'y'
		if row[8] == '':
		  imageCompressionYearMonthDay = "0"
		else:
		  imageCompressionYearMonthDay = row[8]
		if row[9] == '':
		  imageCompressionTime = "0"
		else:
		  imageCompressionTime = row[9]
		if row[10] == '':
		  compressionDST = "0"
		else:
		  compressionDST = row[10]
		if row[11] == '':
		  imageCompressionToolList = "0"
		else:
		  imageCompressionToolList = row[11]
		writeFile()

gatherInput()
