# Ex B.1:

def list_reverse (list1):
    '''  This function take as input a list and returns the reverse of the list 
    without changing the original list. '''
    newList = list1[:]
    newList.reverse()
    return newList


# Ex B.2:

def list_reverse2 (list1):
    ''' This function takes as input a list and returns the reverse of the list 
    without changing the original list. Uses a for loop and range function. '''
    
    list2 = []
    for i in range(len(list1)-1,-1,-1):
        list2.append(list1[i])
    return list2

# Ex B.3

def file_info (nameOfFile):
    ''' This function takes a single input (a string representing the name 
    of a text file), and returns the number of lines, the number of words, and
    the number of characters in the file as a tuple with three components
    (line count, word count, character count). '''
    
    sampleFile = open(nameOfFile, 'r')
    numLines = 0
    numChars = 0
    numWords = 0
    
    for line in sampleFile:
        numLines += 1
        numWords += len(line.split())
        numChars += len(line)
        
    sampleFile.close()
    
    return (numLines, numWords, numChars)

# Ex B.4

def file_info2 (nameOfFile):
    ''' This function inputs the name of a file and finds the number of lines,
    words, and characters and outputs a dictionary with this information '''
    
    fileInfo = {'lines': file_info(nameOfFile)[0],
                'characters': file_info(nameOfFile)[2],
                'words': file_info(nameOfFile)[1]}
    return fileInfo

# Ex B.5

def longest_line (nameOfFile):
    ''' This function takes as input the name of a text file and returns the 
    length of the longest line of the file, as well as the line itself in
    tuple format. '''
    
    sampleFile = open(nameOfFile, 'r')
    lineNum = 0
    longestLine = ''
    currentLine = 0
    
    for line in sampleFile:
        currentLine += 1
        if len(line) > len(longestLine):
            longestLine = line
            lineNum = currentLine
    return (len(longestLine), longestLine)

# Ex B.6

def sort_words (inputString):
    ''' This function takes in a string and splits the string into a list of
    strings which then gets sorted and returned. '''
    
    listofWords = inputString.split()
    listofWords.sort()
    return listofWords

# Ex B.7

# Converting binary number 11011010 to decimal means 0*2^0 + 1*2^1 + 0*2^2
# + 1*2^3 + 1*2^4 + 0*2^5 + 1*2^6 + 1*2^7 which equals . Largest eight - digit
# binary number (11111111) is 255 in decimal. 

# Ex B.8

def binaryToDecimal (listofDigits):
    ''' This function takes a list of 0s and 1s and converts it to a decimal
    integer.'''
    
    decimalInt = 0
    listofDigits.reverse()
    for (i, e) in enumerate(listofDigits):
        decimalInt += e * (2**i)
    return decimalInt

# Ex B.9

def findHowMany2s (number):
    '''This function takes an int and finds the number of twos that the number 
    is most divisble by. Basically returns the greatest power of n such that 
    number / (2^n) is no longer divisble by 2.'''
    
    count = 0
    
    while True:
        if (number) >= 2:
            count += 1
            number = number / 2.0
        else:
            break
    return count

def decimalToBinary (decimalInt):
    ''' This function takes a decimal number and converts it to a list of 
    binary. '''
    
    binary = []
    numberOfBinaryDigits = findHowMany2s(decimalInt)
    
    for i in range(numberOfBinaryDigits,-1,-1):
        if decimalInt / (2**i) >= 1:
            binary.append(1)
            decimalInt -= (2**i)
        else:
            binary.append(0)
    return binary

# Ex C.1: Done

# Ex C.2.1

# The programmer needs to add space after commas, add space between operators, 
# and make the function name useful and relevant.

def sumOfCubes (a, b, c):
    return a * a * a + b * b * b + c * c * c

# Ex C.2.2

# The errors include: Grammatically incorrect comments, a too long return line,
# a need to either use underscores or camelcase for multiple word 
# variable names, and a space after comments

def sumOfCubes (num1, num2, num3):
    # Return sum of cubes of num1, num2, and num3
    return num1 * num1 * num1 + num2 * num2 * num2 + num3 * num3 * num3

# Ex C.2.3

# The programmer needs to add a blank line between two different functions, and
# make the comment a full sentence beginning with a capital letter.

# There are two different kinds of style mistakes here

def sum_of_squares (x, y):
    return x * x + y * y

def sum_of_cubes (x, y, z):
    return x * x * x + y * y * y + z * z * z

        
    
    
            
    
