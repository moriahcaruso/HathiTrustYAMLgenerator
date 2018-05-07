# Goal: To handle labels

# Determines the length of the 000s to ensure that the filename is 8 characters.
def determinePrefixLength(pageNum):
	global prefixZeroes
	if 0 < pageNum < 10:
		prefixZeroes = '0000000'
	elif 10 <= pageNum < 100:
		prefixZeroes = '000000'
	elif 100 <= pageNum < 1000:
		prefixZeroes = '00000'
	elif 1000 <= pageNum < 10000:
		prefixZeroes = '0000'
	else:
		prefixZeroes = 'error'

# Creates the file's name. Combines the leading 0s, integer as string, and filetype, and outputs global variable fileName
def generateFileName(prefix, suffix, fileType):
	global fileName
	fileName = prefix + str(suffix) + '.' + fileType

#  Uses the number of the reading start page to determine where the reading order starts/print.
def generateOrderLabel(readingStartNum, pageNum, orderNum):
	global orderLabel
	orderLabel = ''
	if pageNum >= readingStartNum:
		orderLabel = 'orderlabel: "' + str(orderNum) + '"'

# Processes inputs for various page numbers. Casts everything but covers, because there should only be one, into lists if they're not already lists. Could almost definitely be improved.
def inputToLists():
	global blankPages, chapterPages, chapterStart, copyrightPages, firstChapterStart, foldoutPages, imagePages, indexStart, referenceStartPages, tableOfContentsStarts, titlePages, halfTitlePages
	if type(blankPages).__name__ == 'int':
		blankPages = map(int, str(blankPages))
	if type(chapterPages).__name__ == 'int':
		chapterPages = map(int, str(chapterPages))
	if type(chapterStart).__name__ == 'int':
		chapterStart = map(int, str(chapterStart))
	if type(copyrightPages).__name__ == 'int':
		copyrightPages = map(int, str(copyrightPages))
	if type(firstChapterStart).__name__ == 'int':
		firstChapterStart = map(int, str(firstChapterStart))
	if type(foldoutPages).__name__ == 'int':
		foldoutPages = map(int, str(foldoutPages))
	if type(imagePages).__name__ == 'int':
		imagePages = map(int, str(imagePages))
	if type(indexStart).__name__ == 'int':
		indexStart = map(int, str(indexStart))
	if type(referenceStartPages).__name__ == 'int':
		referenceStartPages = map(int, str(referenceStartPages))
	if type(tableOfContentsStarts).__name__ == 'int':
		tableOfContentsStarts = map(int, str(tableOfContentsStarts))
	if type(titlePages).__name__ == 'int':
		titlePages = map(int, str(titlePages))
	if type(halfTitlePages).__name__ == 'int':
		halfTitlePages = map(int, str(halfTitlePages))

# Handles the reading labels. Uses list function which then gets split apart, so that multiple labels can apply to same page if relevant.
def generateLabel(pageNum):
	global label
	inputToLists()
	labelList = []
# map(int, str(vari)) will cast single variable to list
# Testing whether or not a page has a label
	if pageNum == frontCover:
		labelList.append('"FRONT_COVER"')
	if pageNum == backCover:
		labelList.append('"BACK_COVER"')
	if pageNum in blankPages:
		labelList.append('"BLANK"')
	if pageNum in chapterPages:
		labelList.append('"CHAPTER_PAGE"')
	if pageNum in chapterStart:
		labelList.append('"CHAPTER_START"')
	if pageNum in copyrightPages:
		labelList.append('"COPYRIGHT"')
	if pageNum in firstChapterStart:
		labelList.append('"FIRST_CONTENT_CHAPTER_START"')
	if pageNum in foldoutPages:
		labelList.append('"FOLDOUT"')
	if pageNum in imagePages:
		labelList.append('"IMAGE_ON_PAGE"')
	if pageNum in indexStart:
		labelList.append('"INDEX"')
	if pageNum in referenceStartPages:
		labelList.append('"REFERENCES"')
	if pageNum in tableOfContentsStarts:
		labelList.append('"TABLE_OF_CONTENTS"')
	if pageNum in titlePages:
		labelList.append('"TITLE"')
	if pageNum in halfTitlePages:
		labelList.append('"TITLE_PARTS"')
	if not labelList:
		label = ''
	else:
		label = 'label: ' + ', '.join(labelList)

# Combines all functions to write the file.
def writeFile(finalNumber, readingStartNum, fileType, outputFile):
	f = open(outputFile, 'w')
	pageNum = 1
	orderNum = 1
	while pageNum <= finalNumber:
		determinePrefixLength(pageNum)
		generateFileName(prefixZeroes, pageNum, fileType)
		generateOrderLabel(readingStartNum, pageNum, orderNum)
		generateLabel(pageNum)
		comma = ''
		if orderLabel != '' and label !='':
			comma = ', '
		output = '    ' + fileName + ': { ' + orderLabel + comma + label + ' }\n'
		f.write(output)
		if pageNum >= readingStartNum:
			orderNum += 1
		pageNum += 1
	f.close()

# Putting input into a function vs. having a huge list of inputs at the end.
def gatherInput():
	global fileType, finalNumber, readingStartNum, frontCover, outputFile, backCover, blankPages, chapterPages, chapterStart, copyrightPages, firstChapterStart, foldoutPages, imagePages, indexStart, multiworkBoundaries, prefacePages, referenceStartPages, tableOfContentsStarts, titlePages, halfTitlePages
	outputFile = raw_input("What file to do you want to write this to? ")
	fileType = raw_input("What is the (lowercase) filetype? ")
	finalNumber = input("What is the number of the final image? ")
	print 'When listing multiple numbers, separate them with a ", ".\nSome entries, such as the first chapter, should only have multiple entries if multiple works are bound together and submitted together, generally volumes of the same title. Occasionally something like Index may be repeated within a single work, such as a hymnal.\nWhen a question has no answer, ENTER 0.'
	readingStartNum = input("What is the file number on which page 1 occurs? ")
	frontCover = input("What file number is the front cover? ")
	backCover = input("What is the file number of the back cover? ")
	blankPages = input("List the file numbers of any blank pages: ")
	chapterPages = input("List the file numbers of pages containing only chapter names: ")
	chapterStart = input("List file numbers of the start of each chapter **EXCEPT** the first, including appendices: ")
	copyrightPages = input("List the file number of the title page verso (back of title page containing copyright info) for each work: ")
	firstChapterStart = input("List the file number of the first chapter on a regularly-numbered page (may be Preface) for each work: ")
	foldoutPages = input("List the file number of any page that is a scan of a foldout: ")
	imagePages = input("List the file number of any page which is only an image: ")
	indexStart = input("List the file number of any pages which are the FIRST page of an index: ")
	multiworkBoundaries = input("List the file number of any multi-work boundaries: ")
	prefacePages = input("List the file number of each Preface, defined as sections that appear between the title page verso/copyright and page 1. Do not list any Prefaces beginning on or after page 1: ")
	referenceStartPages = input("List the file number of the first page of any set of references or bibliography: ")
	tableOfContentsStarts = input("List file numbers of the first page of any Table of Contents: ")
	titlePages = input("List file number of any title pages (one per work): ")
	halfTitlePages = input("List the file numbers of any half title pages (preliminary title pages often before the first title page, little or no information on reverse): ")

gatherInput()
writeFile(finalNumber, readingStartNum, fileType, outputFile)