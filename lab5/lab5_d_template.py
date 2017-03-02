from Tkinter import *
import random

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
    global circles
    global color
    
    key = event.keysym
    if key == 'q':
        quit()
    elif key == 'x':
        for c in circles:
            canvas.delete(c)
    elif key == 'c':
        while True:
            newColor = random_color()
            if newColor != color:
                color = newColor
                break
            

def button_handler(event):
    '''Handle left mouse button click events.'''
    global color
    positionTuple = (event.x, event.y)
    diameter = random_size(10, 50)
    circle = draw_random_circle(canvas, color, diameter, positionTuple)
    circles.append(circle)
    

def draw_random_circle(canvas, color, diameter, positionTuple):
    c = canvas.create_oval(positionTuple[0] - diameter / 2.0, \
                           positionTuple[1] - diameter / 2.0, \
                           positionTuple[0] + diameter / 2.0, \
                           positionTuple[1] + diameter / 2.0, \
                           outline = color, fill = color)
    return c

if __name__ == '__main__':
    root = Tk()
    root.geometry('800x800')
    canvas = Canvas(root, width=800, height=800)
    canvas.pack()
    circles = []
    color = random_color()

    # Bind events to handlers.
    root.bind('<Key>', key_handler)
    canvas.bind('<Button-1>', button_handler)

    # Start it up.
    root.mainloop()

