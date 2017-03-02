from Tkinter import *

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
    draw_square(canvas, 'red', 100, (50, 50))
    draw_square(canvas, 'green', 100, (750, 50))
    draw_square(canvas, 'blue', 100, (50, 750))
    draw_square(canvas, 'yellow', 100, (750, 750))
    
    root.mainloop()

    
