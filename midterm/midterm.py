# Name: Andrew Wang
# CMS cluster login name: azwang

import random
import sys
import string


# Problem 1.1

# Error 1: Docstrings should be written using triple quotes, not double quotes

# Error 2: The end of a for statement should end in ':' not ';' 
# 'for item in lst; should be written as 'for item in lst:'

# Error 3: Indentation of if... elif is off (not aligned)

# Error 4: When comparing item and n, one has to use == not = (= is used for
# assignment). So it should be 'elif item == n', not 'elif item = n'

# Error 5: Returning a tuple must be in the form of (qt, eq, lt). The code fails
# to include commas when it says return (qt eq lt)


# Problem 1.2

# Error 1: The 'n -= 1 should go inside the while loop. Otherwise, if n > 0 to 
# start, the while loop will continue to run forever. In addition, even if the
# while loop was never executed because the user inputted 0, the function would
# return (1-1) or 0 not 1 which is the correct value for 0!

# Error 2: factorial (n) is called in the sin(x) function yet the factorial 
# function does not accept any arguments

# Error 3: use = to assign value to tiny not == so it should be written as 
# 'tiny = 1.0e-16

# Error 4: The return statement (after 'if abs(term) < tiny') is called 
# prematurely. This function will never print the result because return 
# automatically exits the function. The programmer can include a break statement
# instead and include a return statement after the loop which will return the
# result

# Error 5: 'print result' should be 'return result' because the function is 
# supposed to return the value, not print it. Printing is pretty useless for 
# the function because most likely, the programmer would like to store the 
# calculated value


# Problem 1.3

# Error 1: The function name is irrelevant. Try to make it somewhat descriptive.
# The variable names could also be more descriptive.

# Error 2: Use triple quotes for docstrings

# Error 3: Add space between variables and the '=' when assigning values

# Error 4: Leave space after the '#' in a comment which isn't done here

# Error 5: Grammatically incorrect docstring

# Error 6: The '#!!!' is a useless comment that should be ommitted

# Error 7: Add space between variables and operator in a comparison, which is
# not done when the coder writes 'if d%2==0'


# Problem 2.1

def random_walk(threshold, numberOfTimes):
    ''' This function takes two arguments, a threshold value, and the amount 
    of times the simulation will be repeated. It records the number of step 
    counts (either +1 or -1) to get to the threshold and after repeating the
    simulation the given number of times, the average of all the step counts
    will be returned. '''
    
    # Seems like the average tends to approach the threhold ^ 2
    
    totalNum = 0
    stepOptions = [-1,1]
    
    for i in range(numberOfTimes):
        position = 0
        stepCount = 0
        while True:
            step = random.choice(stepOptions)
            position += step
            stepCount += 1
            if abs(position) > threshold:
                totalNum += stepCount
                break
    return float(totalNum) / numberOfTimes 

# Problem 2.2

def draw_box(size, prob):
    ''' This function takes two arguments, the size of the interior box and the
    probability of drawing an 'O' for the interior of the box. The box has '+' 
    as corners, '-' as the top and bottom edges, and '|' as the left and right
    edges. '''
    
    assert prob <= 1.0 and prob >= 0.0
    assert size > 0
    
    size += 2     # I added two to size so that I could directly accomodate for 
                  # the borders in the for loops below. 
    
    write = sys.stdout.write
    for row in range(size):
        for col in range(size):
            if row == 0 or row == size - 1:
                if col == 0 or col == size - 1:
                    write ('+')
                else:
                    write ('-')

            else:
                if col == 0 or col == size - 1:
                    write('|')
                else:
                    testProb = random.random()
                    if testProb < prob:
                        write('O')
                    else:
                        write(' ')
        write ('\n')

# Problem 2.3

def initial_value_count(lst):
    ''' This function takes a list and returns a tuple consisting of the first
    value in the argument list and the number of times it is repeated 
    consecutively at the beginning of the list. '''
    
    first = lst [0]
    count = 0
    for i in lst:
        if i == first:
            count +=1
        else:
            break
    return (first, count)

def run_length_encode(lst):
    ''' This function is very similar to the function above, but returns a list
    of tuples as a run-length encoded version of the original list. '''
    
    returnlst = []
    start = 0

    while True:
        if start >= len(lst):
            break
        else: 
            item, repeats = initial_value_count(lst[start:])
            returnlst.append((item, repeats))
            start += repeats
        
    return returnlst
        
# Problem 3.1

def make_subst_dicts():
    ''' This function takes no arguments and outputs a tuple of two 
    dictionaries. These dictionaries are randomly generated and the keys of 
    one dictionary are the values of another and the reverse must also hold
    true. '''
    
    encoding = {}
    decoding = {}
    
    regular = list(string.lowercase)
    scramble = regular [:]
    random.shuffle(scramble)
    
    for i in range(len(regular)):
        encoding [regular[i]] = scramble[i]
        decoding [scramble[i]] = regular[i]
    
    return (encoding, decoding)    
                
# Problem 3.2

def encode_subst(codeDict, codeString):
    ''' This function takes a encoding/decoding dictionary and converts the 
    string argument to an encrypted string using the dictionary. '''
    
    encodedStr = ''
    for i in codeString:
        if i.lower() in codeDict:
            encodedChar = codeDict [i.lower()]
            if i == i.upper():
                encodedChar = encodedChar.upper()
        else:
            encodedChar = i
        
        encodedStr += encodedChar
        
    return encodedStr

# Problem 3.3

def encode_seq(direction, code):
    ''' This function takes two strings. The first string is either 'en' or 'de'
    indicating the encoding direction while the second string is the string to 
    be encoded.'''
    strToInt = {}    # Maps 'a' to 1, 'b' to 2, and so on
    intToStr = {}    # Maps 1 to 'a', 2 to 'b' and so on
    encodedStr = ''
    start = 0
    for i in string.lowercase:
        strToInt[i] = start
        start +=1
    for key,value in strToInt.items():
        intToStr[value] = key
        
    previous = 0
    for i in code:
        if i.lower() not in strToInt:
            encodedStr += i
        else:
            if direction == 'en':
                valueChar = ord(i.lower()) - ord('a') + previous
                previous = valueChar
            else:
                valueChar = ord(i.lower()) - ord('a') - previous
                previous = ord(i.lower()) - ord('a')
            valueChar = valueChar % 26
            if i == i.upper():
                encodedStr += intToStr[valueChar].upper()
            else:
                encodedStr += intToStr[valueChar]
                
    return encodedStr


# Problem 3.4

def encode(direction, dictTuple, code):
    ''' This function takes three arguments: a string representing 'en' or 'de',
    a tuple of encoding/decoding dictionaries, and a string to encode or decode.
    It outputs an encoded string by first applying the sequential code and then
    using the substitution code.
    '''
    if direction == 'en':
        codeDict = dictTuple[0]
        afterSeq = encode_seq(direction, code)
        afterSub = encode_subst(codeDict, afterSeq)   
        return afterSub
    else:
        codeDict = dictTuple[1]
        afterSub = encode_subst(codeDict, code)
        afterSeq = encode_seq(direction, afterSub)
        return afterSeq
        
# Problem 3.5

def encode_file(direction, dictTuple, readFile, writeFile):
    ''' This function takes a string representing 'en' or 'de', a tuple 
    consisting of encoding/decoding dictionaries, filename of the file to 
    encrypt, and the filename of the file to write the encrypted code to. 
    This function will encode/decode the readFile and output it to a
    writeFile.'''
    
    inputFile = open(readFile, 'r')
    outputFile = open(writeFile, 'w')
    for line in inputFile:
        outputFile.write(encode(direction, dictTuple, line))
    inputFile.close()
    outputFile.close()
        
    
    
    
    
    
        
            
        
        
        
    

 
            
            
            