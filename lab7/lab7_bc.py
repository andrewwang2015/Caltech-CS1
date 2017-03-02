# Ex B.1.1

def union(set1, set2):
    ''' This function takes two sets and returns their union as another set.'''
    set3 = set([])
    
    for x in set1:
        set3.add(x)
    for x in set2:
        if x not in set1:
            set3.add(x)
    return set3

# Ex B.1.2

def intersection(set1, set2):
    '''This function computes the intersection of both sets and returns it'''
    
    set3 = set([])
    for i in set1:
        if i in set2:
            set3.add(i)
    return set3

# Ex B.2

def mySum(*x):
    ''' This function takes an arbitrary number of arguments and returns their
    sum. '''
    
    sum1 = 0
    for i in x:
        if type(i) != int:
            raise TypeError('Invalid type: not an integer')
        elif i <= 0:
            raise ValueError('Invalid integer: Negative integer')
        else:
            sum1 += i
    return sum1

# Ex B.3

def myNewSum(*args):
    ''' This function will be able to take a single list of positive integers as
    its only argument and which will return the sum of the list. This function 
    will also be able to take an arbitrary number (zero or more) of individual 
    values (positive integers), but it won't accept both individual values and 
    a list, nor will it accept multiple lists (it will raise a TypeError in 
    such cases)'''
    
    sum1 = 0
    
    if len(args) != 0:
        type1 = type(args[0])
    else:
        return 0
    
    if type1 == list:
        
        if len(args) > 1 and type1 == type(args[1]):
            raise TypeError('Cannot have multiple lists')
        
        for i in args[0]:
            if type(i) != int:
                raise TypeError('List elements not integers')
            elif i < 1:
                raise ValueError('List element less than 1')
            else: 
                sum1 += i
        
    elif type1 == int:
        for i in args:
            if type(i) != int:
                raise TypeError('Invalid type: not an integer')
            elif i <= 0:
                raise ValueError('Invalid integer: Non positive integer')
            else:
                sum1 += i
                
    else:
        raise TypeError('Invalid arguments for function.')
    
    return sum1

# Ex B.4

def myOpReduce(list1, **op):
    '''This function will take one required argument (a list of integers) and 
    one keyword argument called op, whose value should be a string. If op is 
    '+', then the function will sum all the integers; if it's '*', it will 
    multiply them all together, and if it's 'max', it will return the maximum 
    of the numbers'''
    
    product1 = 1
    
    if len(op) < 1:
        raise ValueError('no keyword argument')
    elif len(op) > 1:
        raise ValueError('too many keyword arguments')
    else:
        if 'op' not in op:
            raise ValueError('invalid keyword argument')
        elif op['op'] == '+':
            return sum(list1)
        
        elif op['op'] == '*':
            for i in list1:
                product1 *= i
            return product1
        
        elif op['op'] == 'max':
            if len(list1) == 0:
                return 0
            return max(list1)
        
        elif type(op['op']) != str:
            raise TypeError('value for keyword argument "op" must be a string')
        
        else:
            raise ValueError('invalid keyword argument')
        
# Ex C.1 : This function simply quits after the exception is caught without
# telling the user any useful information about what happened. In addition, it
# does not account for other errors that could occur such as a type error from
# adding/ concatenating two objects that are not compatible. In this
# case, it may also be beneficial to exactly say what corresponding items
# cannot be concatenated /summed. Quitting may also
# not be necessary. Instead of quitting after the key error, the programmer 
# should return a useful error statement on what exactly went wrong. A specific
# message stating which specific key cannot be found would help the user better
# understand what went wrong.

import sys

def sum_of_key_values(dict, key1, key2):
    '''Return the sum of the values in the dictionary stored at key1 and key2'''
    try:
        return dict[key1] + dict[key2]
    except KeyError as e:   
        raise KeyError(str(e) + ' is an invalid key')
    except TypeError as e:
        print "Type Error: " \
        "'%s' and '%s' cannot be summed." %(dict[key1], dict[key2])

# Ex C.2 : This try except does not account for a type error, in which the 
# values may not be of the same type. In such a case, an error message
# that describes what exact elements cannot be summed
# would be helpful. In addition, the Key Error message that
# prints is very general and should be more specific by stating perhaps
# which key could not be found. 

import sys

def sum_of_key_values(dict, key1, key2):
    '''Return the sum of the values in the dictionary stored at key1 and key2'''
    try:
        return dict[key1] + dict[key2]
    except KeyError as e:   
        raise KeyError(str(e) + ' is an invalid key')
    except TypeError as e:
        print "Type Error: " \
        "'%s' and '%s' cannot be summed." %(dict[key1], dict[key2])

# Ex C.3 : The raise is not specific here. Simply raising a KeyError will only
# print 'KeyError:' to the console if a KeyError applies, with no additional 
# information on perhaps which key failed or anything of that sort. In addition,
# similar to the previous examples, a TypeError should be also accounted for.

import sys

def sum_of_key_values(dict, key1, key2):
    '''Return the sum of the values in the dictionary stored at key1 and key2'''
    try:
        return dict[key1] + dict[key2]
    except KeyError as e:   
        raise KeyError(str(e) + ' is an invalid key')
    except TypeError as e:
        print "Type Error: " \
        "'%s' and '%s' cannot be summed." %(dict[key1], dict[key2])

    
# Ex C.4: This program does not need to split up the try and excepts and by 
# doing so, elongates the function unnecessarily. By using one except KeyError
# and using 'as e', one can specify exactly which key is invalid (as shown 
# below). Also, raisinng e in the except blocks of the given function is too 
# general as it would output 'KeyError: ' followed by the name of the input key
# that does not exist, which can be confusing to the user. Lastly, as mentioned
# before, one can accomodate for a type error.
            
def sum_of_key_values(dict, key1, key2):
    '''Return the sum of the values in the dictionary stored at key1 and key2'''
    try:
        return dict[key1] + dict[key2]
    except KeyError as e:   
        raise KeyError(str(e) + ' is an invalid key')
    except TypeError as e:
        print "Type Error: " \
        "'%s' and '%s' cannot be summed." %(dict[key1], dict[key2])        
    
# Ex C.5 : The print statement inside the case when n < 0 never prints but 
# instead if n < 0, the console outputs 'ValueError:' with no explanation of 
# what went wrong. One can combine the print statement and raise exception in
# one line. Also, a type error should also be accomodated for. 

def fib(n):
    '''Return the nth fibonacci number.'''
    if type(n) != int:
        raise TypeError('%s is not an int' %n)
    elif n < 0:
        raise ValueError ('%s is not >= 0' %n)
    elif n < 2:
        return n  # base cases: fib(0) = 0, fib(1) = 1.
    else:
        return fib(n-1) + fib(n-2)

# Ex C.6 : Similar to the previous example, this does not check for the case 
# where n is not an integer. In addition, the printing and raising can be done
# in one step and in which case, the Value Error and message will be on the 
# same line.

def fib(n):
    '''Return the nth fibonacci number.'''
    if type(n) != int:
        raise TypeError('%s is not an int' %n)
    elif n < 0:
        raise ValueError ('%s is not >= 0' %n)
    elif n < 2:
        return n  # base cases: fib(0) = 0, fib(1) = 1.
    else:
        return fib(n-1) + fib(n-2)

# Ex C.7 : This function raises the run type of exception error. If x has to 
# be less than > 0 and the user inputs a negative, it is a value error, NOT a 
# type error as shown in this example. Also, there are conflicts between the
# docstring and the code itself. The docstring says that the function should 
# work for x > 0, but the code only has an if statement for x < 0. What about 
# when x = 0? Because of this, another exception (ZeroDivisionError) has
# to be accounted for. Also, we need to account for when the type of input
# is not a float or int, in which case a type error needs to be raised as well.
# Also, corresponding messages for errors should be specific.

from math import exp

def exp_x_over_x(x):
    '''
    Return the value of e**x / x, for x > 0 and
    e = 2.71828... (base of natural logarithms).
    '''
    
    if type(x) != float and type(x) != int:
        raise TypeError('"%s" is not a float or int' % str(x))
    elif x < 0:
        raise ValueError('%d is not > 0.0' % x)
    elif x == 0:
        raise ZeroDivisionError('x cannot be zero')
    return (exp(x) / x)

# Ex C.8 : This function raises exceptions which are way too general. It should 
# specify what type of exception is raised. For example, if x is not a float or
# int, it should be a type error that should be raised. 
# Same with ValueError and ZeroDivisionError for a negative input or input of 0. 

from math import exp

def exp_x_over_x(x):
    '''
    Return the value of e**x / x, for x > 0 and
    e = 2.71828... (base of natural logarithms).
    '''

    if type(x) != float and type(x) != int:
        raise TypeError('"%s" is not a float or int' % str(x))
    elif x < 0:
        raise ValueError('%d is not > 0.0' % x)
    elif x == 0:
        raise ZeroDivisionError('x cannot be zero')
    return (exp(x) / x)
        

        
            
            
    
        
    


    