# Goal: Take input of final image number, image filetype, and print list of files.

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
		
def generateFileName(prefix, suffix, fileType):
	global fileName
	fileName = prefix + str(suffix) + '.' + fileType

def basicFileNamePrinting(finalNumber, fileType):
	i = 1
	while i <= finalNumber:
		determinePrefixLength(i)
		generateFileName(prefixZeroes, i, fileType)
		print fileName
		i += 1

finalNumber = int(raw_input("What is the number of the final image? "))

fileType = raw_input("What is the (lowercase) filetype? ")

basicFileNamePrinting(finalNumber, fileType)