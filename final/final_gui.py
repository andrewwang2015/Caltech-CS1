# Name: Andrew Wang 
# CMS cluster login name: azwang

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
        dictionary = {'.': 'red', 'a' : 'blue', 'b': 'green', 'c': 'yellow', \
                      'd': 'gray', 'e': 'cyan'}
        sizeHorizontal = self.nrows * 25
        sizeVertical = (self.ncols+1) * 25

        geometryString = str(sizeHorizontal) + 'x' + \
            str(sizeVertical+200)
        self.root.geometry(geometryString)
        self.canvas.config(width=sizeHorizontal, height=sizeVertical)
        
        self.canvas.delete('all')
        initialx = 0
        initialy = 0
        finalx = 25
        finaly = 25
        
        
        
        for i in range(len(self.board)):
            for j in range(len(self.board[0])):
                color2 = dictionary[self.board[i][j]]
                
                r = self.canvas.create_rectangle(initialx, initialy, finalx, \
                                                 finaly, fill=color2, \
                                                 outline=color2)

                initialx += 25
                finalx += 25

            initialx = 0
            finalx = 25
            initialy += 25
            finaly += 25
            
        self.canvas.update()

    
  

    def printBoard(self, board, nmoves, file=sys.stdout):
        '''
        Print a board to a file. 

        Arguments:
          board  -- the board to print
          nmoves -- the number of moves leading up to this board
          file   -- the file to print to (default stdout)

        Return value: none
        '''

        ColorGame.printBoard(self, board, nmoves, file)
        self.displayBoard()

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

        if (self.isLegalMove(row, col, color) == False):
            string = '(' + str(row) + ', ' + str(col) + ', ' + str(color) +')'
            raise MoveError('invalid move: %s' % string)
        listOfSpots = []
        originalColor = self.board[row][col]
        

        
        for j in self.adjacentLocations(row, col):
            if self.board[j[0]][j[1]] == originalColor and \
               self.board[j[0]][j[1]] != color:
                listOfSpots.append(j)
                
        
        self.board[row][col] = color
        self.displayBoard()
        time.sleep(.05)
        
        
        while len(listOfSpots) > 0:
            range1 = len(listOfSpots) - 1
            row1 = listOfSpots[range1][0]
            col1 = listOfSpots[range1][1]


            self.board[row1][col1] = color
            self.displayBoard()
            time.sleep(.05)            
            adjacent1 = self.adjacentLocations(row1, col1)

            for j in adjacent1:
                if self.board[j[0]][j[1]] == originalColor and \
                   self.board[j[0]][j[1]] != color:
                    listOfSpots.insert(0, j)
            listOfSpots.pop()
                

        self.nmoves += 1
        self.updateGameHistory(row, col, color)

if __name__ == '__main__':
    game = ColorGameGUI()
    game.play()


