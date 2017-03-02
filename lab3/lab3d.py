'''
lab3d.py
Simple L-system simulator.
'''

# References: 
#   http://en.wikipedia.org/wiki/L-systems
#   http://www.kevs3d.co.uk/dev/lsystems/
# N.B. http://en.wikipedia.org/wiki/MU_puzzle for midterm?

import math

# ---------------------------------------------------------------------- 
# Example L-systems.
# ---------------------------------------------------------------------- 

# Koch snowflake.
koch = { 'start' : 'F++F++F', 
         'F'     : 'F-F++F-F' }
koch_draw = { 'F' : 'F 1', 
              '+' : 'R 60', 
              '-' : 'L 60' }

# Hilbert curve.
hilbert  = { 'start' : 'A', 
             'A'     : '-BF+AFA+FB-' , 
             'B'     : '+AF-BFB-FA+' }
hilbert_draw = { 'F' : 'F 1', 
                 '-' : 'L 90', 
                 '+' : 'R 90' }

# Sierpinski triangle.
sierpinski = { 'start' : 'F-G-G', 
               'F'     : 'F-G+F+G-F', 
               'G'     : 'GG' }
sierpinski_draw = { 'F' : 'F 1', 
                    'G' : 'F 1', 
                    '+' : 'L 120', 
                    '-' : 'R 120' }

# ---------------------------------------------------------------------- 
# L-systems functions.
# ---------------------------------------------------------------------- 

def update(dictionary, LsystemString):
    ''' This function will generate the next version of the L - system string
    by applying the L-system rules to each character of the string and combining
    the strings into one big string. Inputs are a dictionary containing starting
    string and input rules and an L-system string.'''
    
    newString = ""
    
    for char in LsystemString:
        if char in dictionary:
            newString += dictionary [char]
        else:
            newString += char

    return newString
    
        
def iterate(lsys, n):
    '''It returns the string which results from starting with the starting 
    string for that L-system and updating n times. Inputs are L-system 
    dictionary and an integer n greater than or equal to 0.'''
    
    starting = lsys['start']
    for i in range(n):
        update(lsys, starting)
        starting = update(lsys, starting)
    return starting

def lsystemToDrawingCommands(draw, s):
    '''This program takes a dictionary whose keys are characters in L-system
    strings and whose values are drawing commands and an L system string and 
    returns a list of drawing commands needed to draw the figure corresponding
    to the L-system string.'''
    
    outputList = []
    
    for char in s:
        if char in draw:
            outputList.append(draw[char])
        else:
            outputList.append(char)
            
    return outputList

def convertToRadians (angle):
    '''This function converts a degree angle to radians.'''
    
    return (angle * (math.pi / 180.0))

def nextLocation(x, y, direction, command):
    ''' This function takes current x coordinate, y coordinate, direction, and 
    a command and outputs the next location and direction of the turtle after
    the drawing command was executed.'''
    
    x = float(x)
    y = float(y)
    angleinRadians = convertToRadians(direction)
    
    commandSplit = command.split()
    
    if commandSplit[0] == 'F':
        x += int(commandSplit[1]) * math.cos(angleinRadians)
        y += int(commandSplit[1]) * math.sin(angleinRadians)
    
    if commandSplit[0] == 'R':
        direction -= int(commandSplit[1])
        if direction <= 0:
            direction = 360 - ((direction * -1) % 360)
    
    if commandSplit[0] == 'L':
        direction += int(commandSplit[1])
        if direction >= 360:
            direction = direction % 360
    
    return (x, y, direction)
        
def bounds(cmds):
    '''This function one argument: a list of commands such as those generated 
    by lsystemToDrawingCommands. It computes the bounding coordinates of the 
    resulting drawing, which means the minimum and maximum x and y coordinates 
    ever achieved by the turtle as it moves to make the drawing. The function
    returns a tuple of the (xmin, xmax, ymin, ymax) coordinates, 
    where each coordinate is a float (not an int).'''
    
    
    x_min = 0.0
    x_max = 0.0
    y_min = 0.0
    y_max = 0.0
    
    currentX = 0.0
    currentY = 0.0
    Dir = 0.0
    
    for i in cmds:
        (currentX, currentY, Dir) = nextLocation(currentX, currentY, Dir, i)
        if currentX < x_min:
            x_min = currentX
        if currentX > x_max:
            x_max = currentX
        if currentY < y_min:
            y_min = currentY
        if currentY > y_max:
            y_max = currentY
    
    return (x_min, x_max, y_min, y_max)
        

def saveDrawing(filename, bounds, cmds):
    '''This function takes a filename, bounds of resulting triple, and a list
    of drawing commands and write this information to a file.'''
    
    newFile = open(filename, 'w')
    for i in bounds:
        newFile.write(str(i) + ' ')
    newFile.write ('\n')
    
    for i in cmds:
        newFile.write (i + '\n')

    newFile.close()


def makeDrawings(name, lsys, ldraw, imin, imax):
    '''Make a series of L-system drawings.'''
    print 'Making drawings for %s...' % name
    for i in range(imin, imax):
        l = iterate(lsys, i)
        cmds = lsystemToDrawingCommands(ldraw, l)
        b = bounds(cmds)
        saveDrawing('%s_%d' % (name, i), b, cmds)

def main():
    makeDrawings('koch', koch, koch_draw, 0, 6)
    makeDrawings('hilbert', hilbert, hilbert_draw, 1, 6)
    makeDrawings('sierpinski', sierpinski, sierpinski_draw, 0, 10)
    
# I will try honor roll problem 2 on the resubmit. It is 1:47 am right now...
    


