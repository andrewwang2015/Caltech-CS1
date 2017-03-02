import math

# Problem B.1

class Point:
    '''This class represents a point in 3D space.'''
    
    def __init__(self, x, y, z):
        ''' Initializes values of object '''
        self.x = x
        self.y = y
        self.z = z
    
    def distanceTo(self, anotherPoint):
        ''' This function calculates distance between current point and 
        another point'''
        
        return math.sqrt((self.x - anotherPoint.x)**2 + \
                         (self.y - anotherPoint.y)**2 + \
                         (self.z - anotherPoint.z)**2) 
    
# Problem B.2

class Triangle:
    ''' This triangle class contains 3 points and has a method which
    calculates area of a triangle consisting of these 3 points'''
    
    def __init__(self, point1, point2, point3):
        self.p1 = point1
        self.p2 = point2
        self.p3 = point3
        
    def area(self):
        ''' This function calculates area based on three given points.'''
        
        a = self.p1.distanceTo(self.p2)
        b = self.p2.distanceTo(self.p3)
        c = self.p3.distanceTo(self.p1)
        
        s = (a + b + c) / 2
        
        area = math.sqrt(s * (s - a) * (s - b) * (s - c))
        
        return area
    
# Problem B.3

class Averager:
    ''' Purpose of this class is to store a list of numbers and perform various
    operations on it '''
    
    def __init__(self):
        self.nums = []
        self.total = 0
        self.n = 0
        
    def getNums(self):
        '''This function returns a copy of the list.'''
        
        copy = self.nums[:]
        return copy
    
    def append(self, toAppend):
        ''' This function appends an item to the current list. '''
        
        self.nums.append(toAppend)
        self.total += toAppend
        self.n += 1
    
    def extend(self, list1):
        ''' This function appends a list to the existing list. '''
        
        for i in list1:
            self.nums.append(i)
            self.total += i
            self.n += 1
            
    def average(self):
        ''' This function returns the average of list. If list has no items,
        return 0.0. '''
        
        if len(self.nums) == 0:
            return 0.0
        return float(self.total) / self.n
    
    def limits(self):
        ''' This function returns a tuple of the min and max of the stored list.
        If list is empty, return (0,0). '''
        
        if len(self.nums) == 0:
            return (0,0)
        return (min(self.nums), max(self.nums))

# Problem C.1

# This code is too wordy. You can easily return a boolean statement.

def is_positive(x):
    '''Test if x is positive.'''
    
    return x > 0


# Problem C.2

# This code is too wordy and consists of unnecessary code. Because this code is
# written in a function and only has to return an index number, as soon as there
# is a match for x in the list, it should immediately return that location. The
# return will automatically exit the function, thus saving time and also making
# it more efficient than iterating through the entire list.
# The code should be:

def find(x,lst):
    '''Returns the index into a list where x is found, or -1 otherwise.
    Assume that x is found at most once in the list.'''
    
    for i, item in enumerate(lst):
        if item == x:
            return i
    return -1


# Problem C.3

# This code is unnecessarily inefficient. By placing the return statement at 
# the end of the function and using four if statements, it basically makes the
# program have to do all these tests even if the category is determined after 
# the first or second if statement. Elifs/else or return statements inside the
# if statements should be used. Revised code below

def categorize(x):
    '''Return a string categorizing the number 'x', which should be
        an integer.'''    
    
    if x < 0:
        return 'negative'
    elif x == 0:
        return 'zero'
    elif x > 10 and x < 10:
        return 'small'
    else:
        return 'large'

# Problem C.4

# It is unnecessary to have specific if/elif scenarios for when lst only has 1
# or 2 items because the sum for any number of items can be generalized using 
# a for loop. Having all these test cases is very inefficient. 

def sum_list(lst):
    '''Returns the sum of the elements of a list of numbers.'''
    
    total = 0
    for i in lst:
        total += i
    return total


    
        
        
        
                
        