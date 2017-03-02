from Tkinter import *
import random
import math

# Graphics commands.

def random_color():
    ''' This function will generate random color values in the format recognized
    by Tkinter (#RRGGBB).'''
    
    possibilities = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 'a', 'b', 'c', 'd', 'e', 'f']
    
    returnString = '#'
    for i in range(6):
        returnString += str(random.choice (possibilities))
    
    return returnString


def random_size(a, b):
    ''' This function returns a random number between a and b. '''
    
    assert a >= 0
    assert b >= 0
    assert a < b
    
    return random.choice(range(a, b))

# Event handlers.

def key_handler(event):
    '''Handle key presses.'''
    
    global lines
    global color
    global N_shaped
    
    key = event.keysym
    if key == 'q':
        quit()
    elif key == 'x':
        for l in lines:
            canvas.delete(l)
        lines = []
    elif key == 'plus':
        N_shaped += 2
    elif key == 'minus' and N_shaped != 5:
        N_shaped -= 2
    elif key == 'c':
        while True:
            newColor = random_color()
            if newColor != color:
                color = newColor
                break
            
def draw_star(canvas, coordinates):
    '''This function takes in a list of coordinates (tuples) and calls the
    draw lines for the set of coordinates. '''
    
    for i in range(N_shaped):
        i_coordinates = coordinates[i]
        i_next = coordinates[(i + (((N_shaped - 1) / 2))) % N_shaped]
        line = draw_line(canvas, i_coordinates[0] , i_coordinates[1], \
                     i_next[0], i_next[1])
        lines.append(line)    
    
def button_handler(event):
    '''Handle left mouse button click events.'''

    positionTuple = (event.x, event.y)
    radius = random_size(50, 100)
    coordinates = calculateCoordinates(positionTuple, radius)
    draw_star(canvas, coordinates)
  

def calculateCoordinates(position, radius):
    '''This function takes an input of a tuple containing the x and y 
    coordinates of the mouse click and appends a tuple of coordinates for 
    where the vertices are. '''
    
    coordinates = []
    x_init = position[0]
    y_init = position[1]
    angle = math.pi / 2
    for i in range(N_shaped):
        coordinates.append(((x_init + radius * math.cos(angle)), \
                            (y_init - radius * math.sin(angle))))
        angle += (2 * math.pi / N_shaped)
    return coordinates 
    
def draw_line(canvas, x1, y1, x2, y2):
    '''Draws a line from (x1,y1) to (x2,y2) in a specific color'''
    
    l = canvas.create_line(x1, y1, x2, y2, fill=color, width=3)
    return l
    

if __name__ == '__main__':
    root = Tk()
    root.geometry('800x800')
    canvas = Canvas(root, width=800, height=800)
    canvas.pack()
    lines = []
    color = random_color()
            
    N_shaped = 5
    

    # Bind events to handlers.
    root.bind('<Key>', key_handler)
    canvas.bind('<Button-1>', button_handler)

    # Start it up.
    root.mainloop()

