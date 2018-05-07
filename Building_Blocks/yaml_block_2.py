# Goal: Print list of images in proper YAML format.
# Goal: Write list to file (take name as input).

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
		
def generateFileName(prefix, suffix, fileType):
	global fileName
	fileName = prefix + str(suffix) + '.' + fileType

def writeFile(finalNumber, readingStartNum, fileType, outputFile):
	f = open(outputFile, 'w')
	pageNum = 1
	while pageNum <= finalNumber:
		determinePrefixLength(pageNum)
		generateFileName(prefixZeroes, pageNum, fileType)
		output = '\t' + fileName + ': { orderlabel: "[futurevar]" }\n'
		f.write(output)
		pageNum += 1
	f.close()

finalNumber = int(raw_input("What is the number of the final image? "))

fileType = raw_input("What is the (lowercase) filetype? ")

readingStartNum = int(raw_input("What is the file number on which page 1 occurs? "))

outputFile = raw_input("What file to do you want to write this to? ")

writeFile(finalNumber, readingStartNum, fileType, outputFile)