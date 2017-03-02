'''
final_gui.py: The CS 1 final exam, part 2.
'''

import sys, copy, time
from Tkinter import *
from final import *

class ColorGameGUI(ColorGame):
    def __init__(self):
        '''
        Initialize the game.

        Arguments: none
        Return value: none
        '''
        # Supplied to the students.  DO NOT MODIFY!

        # Call the superclass constructor on this object.
        ColorGame.__init__(self)
        
        # Tkinter code for display.
        # Nominal starting size of 100x100 pixels.
        self.root = Tk()
        self.root.geometry('100x100')
        self.canvas = Canvas(self.root, width=100, height=100)
        self.canvas.pack(fill='both', expand=True)

    def displayBoard(self):
        '''
        Update a Tkinter canvas showing the board contents.

        Arguments: none
        Return value: none
        '''

        pass # TODO

    def printBoard(self, board, nmoves, file=sys.stdout):
        '''
        Print a board to a file. 

        Arguments:
          board  -- the board to print
          nmoves -- the number of moves leading up to this board
          file   -- the file to print to (default stdout)

        Return value: none
        '''

        pass # TODO

    def makeMove(self, row, col, color):
        '''
        Make a move on the  board by changing the color of the square at (row,
        col) to 'color'.  Raise a MoveError exception if the move is invalid.

        Arguments:
          row   -- the row on the board
          col   -- the column on the board
          color -- the desired color (a letter from a-e or '.')

        Return value: none
        '''

        pass # TODO

if __name__ == '__main__':
    game = ColorGameGUI()
    game.play()

