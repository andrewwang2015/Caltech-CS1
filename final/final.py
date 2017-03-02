# Name: Andrew Wang 
# CMS cluster login name: azwang

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
        try:
            sampleFile = open(filename, 'r')
        except IOError:
            raise LoadError('%s does not exist' %filename)
        
        self.nmoves  = 0
        line1 = sampleFile.readline().strip()
        line1_noSpaces = str(line1.replace(' ', ''))
        line1_modified = str(line1_noSpaces.replace('-',''))
        numSpaces = 0
        spaceLocations = []
        for i in range(len(line1)):
            if line1[i] == ' ':
                numSpaces += 1
                spaceLocations.append(i)

        
        
        if not (line1_modified.isdigit()):
            raise LoadError('First line: "%s" does not consist '\
                            'solely of integers' %line1) 
        if numSpaces != 2:
            raise LoadError('First line: "%s" does not contain '\
                            'three valid integers.' %line1)
        if '-' in line1_noSpaces:
            negativeIndex = line1_noSpaces.index('-')
            if negativeIndex == 0 or line1_noSpaces[0] < 1:
                raise LoadError('Row count out of range')
            elif negativeIndex == 1 or line1_noSpaces[1] < 1:
                raise LoadError('Column count out of range')
            elif negativeIndex == 2:
                raise LoadError('Target out of range')
        
        self.nrows = int(line1[0:spaceLocations[0]])        
        self.ncols = int(line1[spaceLocations[0]: spaceLocations[1]])
        self.target = int(line1[spaceLocations[1]:])            

        numRows = 0
        numCols = 0
 
        
        for line in sampleFile:

            sampleList = []
            
            line = line.strip()
            
            numRows += 1
            numCols = len(line) 

            if numCols != self.ncols:
                raise LoadError('Invalid number of colors in a row')
            for i in line:
                if i not in self.ok_colors:
                    raise LoadError('Row contains invalid color character')          


            sampleList = list(line)
            self.board.append(sampleList)          

        if numRows != self.nrows:
            raise LoadError('Number of rows do not match')
        
        originalBoard = copy.deepcopy(self.board)
        self.history.append((False, originalBoard))

        sampleFile.close()        

    def printBoard(self, board, nmoves, file=sys.stdout):
        '''
        Print a board to a file. 

        Arguments:
          board  -- the board to print
          nmoves -- the number of moves leading up to this board
          file   -- the file to print to (default stdout)

        Return value: none
        '''

        
        file.write('    ')
        firstRow = ''
        for i in range(self.ncols):
            firstRow += str(i)
        file.write(firstRow + '\n')

        file.write('  +')
        file.write('-' * (self.ncols + 1) + '\n')
        for i in range(self.nrows):
            if i//10 >= 1:
                file.write(str(i) + '|' + ' ') 
            else:
                file.write(str(i) + ' ' + '|' + ' ') 
            
            for j in board[i]:
                file.write(j)
            file.write('\n')
        file.write('\n')
        file.write('MOVES: ' + str(nmoves) + '\n')
        file.write('TARGET: ' + str(self.target) + '\n')
        file.write('\n \n')

        
            
        

    def saveGameHistory(self, filename):
        '''
        Save the game history to a file.

        Arguments:
          filename -- name of file to save to

        Return value: none
        '''
        try:
            saveFile = open(filename, 'a')
        except IOError:
            raise saveError('File not found.')
        
        moveCount = 1
        
        for (i,j) in self.history:
            if i == False:

                self.printBoard(j, 0, saveFile)
                
            else:

                string = str(i[2]) + ' at (' + str(i[0]) + ', ' + str(i[1]) + \
                    ')'
                saveFile.write('MOVE : ' + string + '\n \n')

                self.printBoard(j, moveCount, saveFile)
                moveCount += 1
        saveFile.close()
                

    def adjacentLocations(self, row, col):
        '''
        Return a list of the orthogonally adjacent locations to the location at
        (row, col).  Invalid locations (i.e. off the board) are not returned.
        '''

        adjacent = []
        limitingRows = self.nrows - 1
        limitingCols = self.ncols - 1
        
        if (row + 1) <= limitingRows:
            adjacent.append((row + 1, col))
        if (row - 1) >= 0:
            adjacent.append((row - 1, col))
        if (col + 1) <= limitingCols:
            adjacent.append((row, col + 1))
        if (col - 1) >= 0:
            adjacent.append((row, col-1))
        return adjacent

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
        if type(row) != int or type(col) != int or color not in self.ok_colors:
            return False
        if row not in range(0, self.nrows) or col not in range(0, self.ncols):
            return False
        if self.board[row][col] == color:
            return False
        flag = 0
        for i in self.board:
            for j in i:
                if j == color:
                    flag = 1
                    break
        if flag == 0:
            return False
        return True
    
        

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

        while len(listOfSpots) > 0:

            row1 = listOfSpots[0][0]
            col1 = listOfSpots[0][1]


            self.board[row1][col1] = color
            adjacent1 = self.adjacentLocations(row1, col1)

            for j in adjacent1:
                if self.board[j[0]][j[1]] == originalColor and \
                   self.board[j[0]][j[1]] != color:
                    listOfSpots.append(j)
            del listOfSpots[0]
                

        self.nmoves += 1
        self.updateGameHistory(row, col, color)


    def updateGameHistory(self, row, col, color):
        '''
        Add the current move and the current board state to the history.

        Arguments:
          row   -- the row component of the current move
          col   -- the column component of the current move
          color -- the color component of the current move

        Return value: none
        '''

        currentBoard = copy.deepcopy(self.board)
        tuple1 = (row, col, color)
        self.history.append((tuple1, currentBoard))

    def undoMove(self):
        '''
        Undo the last move, adjusting the game history accordingly.

        Arguments: none
        Return value: none
        '''

        if len(self.history) == 1:
            raise MoveError('No last move')
        self.history.pop()
        self.nmoves -= 1
        print len(self.history)
        self.board = copy.deepcopy(self.history[len(self.history)-1][1])
            

    def isGameOver(self):
        '''
        Return True if the game is over (all squares the same color);
        else return False.

        Arguments: none
        '''

        test = self.board[0][0]
        
        for i in range(len(self.board)):
            for j in range(len(self.board[0])):
                if self.board[i][j] != test:
                    return False
        return True

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

        if self.isGameOver():
            if self.nmoves <= self.target:
                return 'WIN'
            elif self.nmoves == self.target + 1:
                return 'DRAW'
            elif self.nmoves > self.target + 1:
                return 'LOSE'
        return 'ONGOING'

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

    

