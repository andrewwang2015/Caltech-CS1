import random
from Tkinter import *

def random_size(a, b):
    ''' This function takes two inputs: both non-negative even integers with 
    the first argument less than the second and returns a random even integer
    which is >=lower number and <= the upper number. '''
    
    assert a >= 0
    assert b >= 0
    assert a < b
    
    return random.choice(range(a, b, 2))

 
def random_position(a, b):
    ''' This function will take two arguments which are > = 0 and will return 
    a tuple with two numbers that are less than the arguments and greater than
    0.'''
    
    return (random.randint(0, a), random.randint(0, b))


def random_color():
    ''' This function will generate random color values in the format recognized
    by Tkinter (#RRGGBB).'''
    
    possibilities = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 'a', 'b', 'c', 'd', 'e', 'f']
    
    returnString = '#'
    for i in range(6):
        returnString += str(random.choice (possibilities))
    
    return returnString


def draw_square(canvas, color, sideLength, positionTuple):
    ''' This function takes four arguments: canvas, color, side length of
    square, and a tuple of the position of the center of the square 
    and will draw the corresponding square and return the handle of the 
    rectangle that was drawn. '''
    
    r = canvas.create_rectangle(positionTuple[0] - sideLength / 2.0, \
                           positionTuple[1] - sideLength / 2.0, \
                           positionTuple[0] + sideLength / 2.0, \
                           positionTuple[1] + sideLength / 2.0,
                           fill = color, outline = color)
    return r
    
    
if __name__ == '__main__': 
    root = Tk()
    root.geometry('800x800')
    canvas = Canvas(root, width=800, height=800)
    canvas.pack() 
    for i in range(50):
        draw_square(canvas, random_color(), random_size(20, 150), \
                    (random_position(800, 800)))
    root.bind('<q>', quit)
    root.mainloop()

    