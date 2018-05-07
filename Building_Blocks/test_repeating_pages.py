import re, os

# To-do: set variables. If the page IN the list, THEN the variable now == that page.

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

#  Uses the number of the reading start page to determine where the reading order starts/print.
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

# What if we did just readingStartNum & readingEndNum generation using this and globals!
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
	inputToLists()
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
	f.write('pagedata:\n')
	fileNum = 1
	orderNum = 1
	romanInt = 1
	multiworkEndList = [0]
	romanEndList = [0]
	if multiworkBoundaries != 0:
		defineMultiWorkLists()
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
	workingDir = "/users/rtillman/documents/projects/hathitrust"
	outputFile = "meta_test_py.yml"
	fileType = "tif"
	finalNumber = 360
	frontCover = 1
	halfTitlePages = 0
	titlePages = (13, 163, 290)
	copyrightPages = (14, 164, 291)
	tableOfContentsStarts = (356, 166)
	romanStart = 3
	romanCap = 9
	prefacePages = 0
	readingStartNum = 13
	firstChapterStart = 15
	chapterPages = 0
	chapterStart = (28, 55, 72, 150, 177, 183, 224, 242, 325, 332, 333, 334, 339, 350)
	readingEndNum = 351
	blankPages = (2, 3, 4, 5, 6, 7, 8, 9, 10, 357, 358, 359)
	unpaginatedPages = 0
	imagePages = 0
	foldoutPages = 0
	indexStart = 0
	referenceStartPages = 0
	multiworkBoundaries = 0
	backCover = 360

gatherInput()
writeFile(finalNumber, readingStartNum, readingEndNum, fileType, outputFile, romanCap, workingDir)
