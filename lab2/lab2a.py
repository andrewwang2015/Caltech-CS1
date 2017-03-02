import random

# Ex B.1:

def complement (DNA):
    '''This function takes a DNA string containing 'A','C', 'G', or 'T and
    returns the complement.'''
    
    complement = ""
    for basePair in DNA:
        if basePair == 'A':
            complement += 'T'
        elif basePair == 'T':
            complement += 'A'
        elif basePair == 'G':
            complement += 'C'
        else:
            complement += 'G'
    return complement

# Ex B.2

def list_complement (DNA):
    ''' This function takes in DNA written as a list of individual base pairs
    and changes each individual base pair to its complement.'''
    
    for i in range(len(DNA)):
        if DNA[i] == 'A':
            DNA [i] = 'T'
        elif DNA[i] == 'G':
            DNA [i] = 'C'
        elif DNA[i] == 'C':
            DNA [i] = 'G'
        else:
            DNA[i] = 'A'

# Ex B.3

def product (numList):
    ''' This function takes in a list of numbers and returns its product. If 
    the list is empty, it will return 1.'''
    
    product = 1
    if len(numList) == 0:
        return 1
    for i in numList:
        product = product * i
    return product

# Ex B.4

def factorial (num):
    '''This function takes in a number and returns its factorial. 0! is taken 
    to be 1.'''
    
    if num == 0:
        return 1
    return product (range(1, num+1,1))

# Ex B.5

def dice (m,n):
    ''' This function takes two arguments, m, the number of sides of the dice,
    and n, the number of dice rolled. This function will compute and return
    the sum of all the random dice values rolled.'''
    
    sumOfDice = 0
    for i in range (n):
        sumOfDice += int(random.choice(range(1,m+1,1)))
    return sumOfDice
    
# Ex B.6

def remove_all (list1, value):
    ''' This function takes a list and a particular integer value and removes
    ALL occurences of that integer value in the list'''
    
    i = 0
    while list1.count(value) >= 1:
        list1.remove(value)

# Ex B.7

def remove_all2 (list1,value):
    '''This function removes all occurences of 'value' from 'list1' by
    counting the number of values to be removed once and then using the remove
    method that many times'''
    
    for i in range(list1.count(value)):
        list1.remove(value)

def remove_all3 (list1,value):
    '''This function removes all occurences of 'value' from 'list1' by finding
    whether or not the value is in the list and removing the value until 
    there is no more left.'''
    
    while value in list1:
        list1.remove(value)
        
# Ex B.8

def any_in (list1, list2):
    '''This function takes two lists and returns true or false based on whether
    or not the two lists share any elements.'''
    
    for x in list1:
        if x in list2:
            return True
    return False

# Ex C.1.a

# One has to use '==' to compare two values. In this case, '=' is used which is
# incorrect because '=' is reserved for assignment of values

# Ex C.1.b

# The argument is the literal string 's', not a variable so s variable is not
# defined. The programmer should change the argument to s without the quotes

# Ex C.1.c

# This is the reverse of what happened in part b. This function will always 
# return 's-Caltech' because its return statement concatenates 's' and 
# '-Caltech'. The return statement should concatenate the argument s (without
# quotes) and -'Caltech'

# Ex C.1.d

# One cannot concatenate a string to a list, one can only concatenate lists.
# To fix this, one can use the append function and write 'lst.append ('bam') or
# make another list ['bam'] and concatenate this lst with the original lst

# Ex C.1.e

# lst.reverse() automatically changes lst, so we do not have to create a new 
# list. So, we can simply write lst.reverse() and then lst.append(0) to make lst
# the reverse of itself with an appended 0. There is also no need for a return
# statement because lists are mutable in Python. If we wanted to preserve the 
# original list, we can create a copy by writing : for x in lst: lst2.append(x)
# and then write lst2.reverse() and lst2.append(0)

# Ex C.1.f

# First off, the arguments are Python keywords representing data types, so
# the arguments have to be renamed for the function to run without error. Even
# if we change the argument names to proper names of variables, the program will
# append a list of letters of the string to the input list, NOT extend it. The 
# difference is as follows (we set x = [1,3,5,1]): x.append (['a','b']) will 
# yield [1,3,5,1,'[a','b']] while x.extend (['a','b']) will yield
# [1,3,5,1,'a','b']. If we want to merge lists completely, extend must be used.

# Ex C.2

# The value of a is changed AFTER c is computed so c takes the old value of a 
# (10) to compute its value (10+20 = 30)

# Ex C.3

# The first option is calling a function that returns a number that can then
# be multiplied by 2 and saved into n. The second option has a function that 
# prints the value, but does not return it. One cannot multiply this print 
# command by 2 which gives an error. Printing a result in a function does 
# exactly that. It prints the value of the temporary variable when the function
# is called, but without a return statement, that value cannot be saved outside
# of the function. A return variable is more versatile. It returns the value
# so that it can be stored in a variable outside of the function which can then
# be manipulated, printed, etc.

# Ex C.4

# The first option works because you are passing the right amount of arguments 
# and the function is returning a value that can be mathematically operated on. 
# The second one does not work because the function accepts no arguments, but
# the function call assumes that the function has two arguments, thus generating
# an error. Passing a value as an argument to a function preserves the values of
# these arguments outside the function because the function creates local 
# variables for these arguments. The raw_input is different because once that
# is called in the function, there is no way to get the values of what the user
# inputs outside of the function. In the second option for this example, without
# returning x and y, there is no way to know what the user inputted because the
# values are confined to the function. 

# Ex C.5

# Strings are immutable so one cannot change the value of the individual 
# characters which the function is attempting to do here. Even if this function
# were to work, it's pretty useless because it does nothing with s (no return

# Ex C.6

# This function will not work as intended because it takes each item in the list
# and does double it, but fails to replace the original item's position in the
# list. To fix this, we would have to keep track of the index and do:
# for x in range(len(lst)):
#     lst[x] *= 2




