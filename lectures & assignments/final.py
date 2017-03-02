'''
final.py: The CS 1 final exam, part 1.
'''

import sys, copy, time

class LoadError(Exception):
    pass

class SaveError(Exception):
    pass

class MoveError(Exception):
    pass

class ColorGame:
    def __init__(self):
        '''
        Initialize the game.

        Arguments: none
        Return value: none
        '''
        # Supplied to the students.  DO NOT MODIFY!
        self.ok_colors = '.abcde'
        self.reset()
        
    def reset(self):
        '''
        Reset the fields of this object to their initial values.

        Arguments: none
        Return value: none
        '''
        # Supplied to the students.  DO NOT MODIFY!
        self.status  = 'ONGOING'
        self.nrows   = 0
        self.ncols   = 0
        self.target  = -1
        self.board   = []
        self.nmoves  = 0
        self.history = []


    def load(self, filename):
        '''
        Load a game board from a file.

        The file format is as follows: 

        The first line contains three numbers: the number of rows, the number of
        characters per line, and the number of moves needed to solve the problem
        (the target).  Each subsequent line consists of single characters from
        a-e or '.', with the correct number of characters per line (not counting
        the ending newline).  If there are any errors (file not found, lines of
        the wrong length, or characters other than a-e or .), a LoadError
        exception is raised.

        Assuming the file is the right format, this method sets the 'board'
        and 'target' fields of the function to the correct values.  'board'
        contains the game board as a list of lists of characters (where each
        inner list is a single row), and 'target' is the number of moves needed
        to solve the puzzle.  This method also sets the 'nrows' and 'ncols'
        fields to their correct values.

        Arguments:
          filename -- name of file to load from

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

    def saveGameHistory(self, filename):
        '''
        Save the game history to a file.

        Arguments:
          filename -- name of file to save to

        Return value: none
        '''

        pass # TODO

    def adjacentLocations(self, row, col):
        '''
        Return a list of the orthogonally adjacent locations to the location at
        (row, col).  Invalid locations (i.e. off the board) are not returned.
        '''

        pass # TODO

    def isLegalMove(self, row, col, color):
        '''
        Return True if a move of (row, col, color) is valid.
        For a move to be valid, the (row, col) coordinates
        must be on the board, and the color must already
        exist somewhere on the board.  In addition,
        the color must not be the same as the existing color
        at location (row, col).

        Arguments:
          row   -- the row component of the move (an integer)
          col   -- the column component of the move (an integer)
          color -- the color component of the move (a character)
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

    def updateGameHistory(self, row, col, color):
        '''
        Add the current move and the current board state to the history.

        Arguments:
          row   -- the row component of the current move
          col   -- the column component of the current move
          color -- the color component of the current move

        Return value: none
        '''

        pass # TODO

    def undoMove(self):
        '''
        Undo the last move, adjusting the game history accordingly.

        Arguments: none
        Return value: none
        '''

        pass # TODO

    def isGameOver(self):
        '''
        Return True if the game is over (all squares the same color);
        else return False.

        Arguments: none
        '''

        pass # TODO

    def gameStatus(self):
        '''
        Update and return the 'status' field of the game.

        If the game is over, the status becomes:
        -- 'WIN'  if the number of moves is <= the target
        -- 'DRAW' if the number of moves = target + 1
        -- 'LOSE' if the number of moves is > target + 1
        If the game is not over, the status is 'ONGOING'.

        Arguments: none
        Return value: the status
        '''

        pass # TODO

    def play(self):
        '''
        Play a game interactively.

        Interactive commands:
          q          -- quit
          l filename -- load a game board from the file named 'filename'
          s filename -- save the game history to a file named 'filename'
          m r c col  -- make a move at row/col location (r, c) with color 'col'
          u          -- undo last move

        After each move or load, the board is printed.

        Invalid or nonexistent commands cause the game to raise a MoveError
        exception with an appropriate error message, which will be caught in
        this function (see below).

        Once the game is over, this function computes and prints the game
        status.  If the result is WIN or DRAW, it then prompts for a filename to
        save the game history to.  Then it exits.

        This function catches MoveError exceptions, prints the error messages,
        and continues. 

        This function also catches LoadError and SaveError exceptions, prints
        the error messages, and exits the function.

        Arguments: none
        Return value: none
        '''
        
        # Supplied to the students.  DO NOT MODIFY!
        while True:
            try:
                cmd = raw_input('Command: ')
                words = cmd.split()
                if len(words) < 1:
                    raise MoveError('No command given.')
                cmd1 = words[0]

                if cmd1 == 'q':
                    if len(words) != 1:
                        raise MoveError('usage: q')
                    break
                elif cmd1 == 'l':
                    if len(words) != 2:
                        raise MoveError('usage: l <filename>')
                    filename = words[1]
                    self.load(filename)
                    self.printBoard(self.board, self.nmoves)
                elif cmd1 == 's':
                    if len(words) != 2:
                        raise MoveError('usage: s <filename>')
                    filename = words[1]
                    self.saveGameHistory(filename)
                elif cmd1 == 'm':
                    if len(words) != 4:
                        raise MoveError('usage: m <row> <col> <color>')
                    try:
                        row = int(words[1])
                        col = int(words[2])
                        color = words[3]
                    except ValueError:
                        raise MoveError('invalid move: %s' % cmd)

                    self.makeMove(row, col, color)
                    self.printBoard(self.board, self.nmoves)
                    if self.isGameOver():
                        status = self.gameStatus()
                        print 'RESULT: %s' % status
                        if status in ['WIN', 'DRAW']:
                            msg = "Enter filename to save to, or 'q' to quit: "
                            savefile = raw_input(msg)
                            if savefile != 'q':
                                self.saveGameHistory(savefile)
                        break
                elif cmd1 == 'u':
                    if len(words) != 1:
                        raise MoveError('usage: u')
                    self.undoMove()
                    self.printBoard(self.board, self.nmoves)
                else:
                    raise MoveError('Invalid command: %s' % cmd1)
            except MoveError as e:
                print e
            except LoadError as e:
                print e
                break
            except SaveError as e:
                print e
                break

if __name__ == '__main__':
    game = ColorGame()
    game.play()

