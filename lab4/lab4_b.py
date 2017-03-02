import Tkinter
import random

# Ex B.1

def random_size(a, b):
    ''' This function takes two inputs: both non-negative even integers with 
    the first argument less than the second and returns a random even integer
    which is >=lower number and <= the upper number. '''
    
    assert a >= 0
    assert b >= 0
    assert a < b
    assert a % 2 == 0
    assert b % 2 == 0
    
    x = random.choice(range(a, b, 2))
    assert x % 2 == 0
    return x

# Ex B.2   

def random_position(a, b):
    ''' This function will take two arguments which are > = 0 and will return 
    a tuple with two numbers that are less than the arguments and greater than
    0.'''
    
    return (random.randint(0, a), random.randint(0, b))

# Ex B.3

def random_color():
    ''' This function will generate random color values in the format recognized
    by Tkinter (#RRGGBB).'''
    
    possibilities = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 'a', 'b', 'c', 'd', 'e', 'f']
    
    returnString = '#'
    for i in range(6):
        returnString += str(random.choice (possibilities))
    
    return returnString

# Ex B.4

def count_values(dictOfDistinct):
    ''' This function takes a single dictionary as an argument and returns a 
    count of the number of distinct values it contains. '''
    
    count = 0
    listOfValues = dictOfDistinct.values()
    while (len(listOfValues)> 0):
        i = listOfValues[0]
        count +=1
        while i in listOfValues:
            listOfValues.remove(i)
    return count

# Ex B.5

def remove_value(dict1, value):
    ''' This function takes a dictionary and an arbitrary item which could be a
    value in the dictionary. It removes (using the del operator) all key/value
    pairs from the dictionary which have that value. '''
    
    listOfKeys = []
    
    for key in dict1:
        if dict1[key] == value:
            listOfKeys.append(key)
    
    for i in listOfKeys:
        del dict1[i]

# Ex B.6

def split_dict(dict1):
    ''' This function takes as its argument a dictionary which uses strings as 
    keys and returns a tuple of two dictionaries whose key/value pairs are from
    the original dictionary: those whose keys start with the letters a-m 
    (lower- or uppercase) and those whose keys start with the letters n-z
    (lower- or uppercase). '''
    
    dict2 = {}
    dict3 = {}
    
    for key in dict1:
        if key.lower() >= 'a' and key.lower() <= 'm':
            dict2[key] = dict1[key]
        if key.lower() >= 'n' and key.lower() <= 'z':
            dict3[key] = dict1[key]
    return (dict2, dict3)

# Ex B.7

def count_duplicates(dict1):
    ''' This function takes a dictionary as an argument and returns the number 
    of values that appear two or more times.'''
    
    count = 0
    list1 = dict1.values()
    
    while len(list1) > 0:
        i = list1[0]
        if list1.count(i) >= 2:
            count += 1
        while i in list1:
            list1.remove(i)
    return count


            
    