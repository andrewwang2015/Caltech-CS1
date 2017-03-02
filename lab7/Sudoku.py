'''
This program allows the user to interactively play the game of Sudoku.
'''

import sys

class SudokuError(Exception):
    pass

class SudokuMoveError(SudokuError):
    pass

class SudokuCommandError(SudokuError):
    pass

class Sudoku:
    '''Interactively play the game of Sudoku.'''

    def __init__(self):
        self.board = [[0]*9 for i in range(9)]
        self.moves = []

    def load(self, filename):
        '''Loads a board from a given filename'''
        
        self.moves = []
        sampleFile = open(filename, 'r')
        numLines = 0
        numChars = 0
        lineCount = 0
        colCount = 0        
        for line in sampleFile:
            numLines += 1
            if numLines > 9:
                raise IOError('More than nine lines')
            numChars = len(line) 
            if numChars != 10 and numLines != 9:
                raise IOError('More than nine characters in line')
            
            line = line[:9]
            for i in line:
                if i not in '0123456789':
                    raise IOError('Digits from 0 - 9 only')            
            for i in line:
                self.board[lineCount][colCount] = int(i)
                colCount += 1
            lineCount += 1
            colCount = 0
            
        sampleFile.close()

    def save(self, filename):
        '''Saves the current board status to file with given filename'''
        
        sampleFile = open(filename, 'w')
        for i in range(9):
            for j in range(9):
                sampleFile.write(str(self.board[i][j]))
            sampleFile.write('\n')
        sampleFile.close()
        

    def show(self):
        '''Pretty-print the current board representation.'''
        
        print
        print '   1 2 3 4 5 6 7 8 9 '
        for i in range(9):
            if i % 3 == 0:
                print '  +-----+-----+-----+'
            sys.stdout.write('%d |' % (i + 1))
            for j in range(9):
                if self.board[i][j] == 0:
                    sys.stdout.write(' ')
                else:
                    sys.stdout.write('%d' % self.board[i][j])
                if j % 3 != 2 :
                    sys.stdout.write(' ')
                else:
                    sys.stdout.write('|')
            print 
        print '  +-----+-----+-----+'
        print

    def move(self, row, col, val):
        '''Takes a row, col and value to place at row, col if valid'''
        
        test1 = (row - 1) // 3
        test2 = (col - 1) // 3
                
        if test1 == 0:
            beginRow = 0
        elif test1 == 1:
            beginRow = 3
        else:
            beginRow = 6
            
        if test2 == 0:
            beginCol = 0
        elif test2 == 1:
            beginCol = 3
        else:
            beginCol = 6
        
               
        if type(row) != int or type(col) != int:
            raise SudokuMoveError('Invalid row/ col inputs')
        if (row < 1 or row > 9) or (col < 1 or col > 9):
            raise SudokuMoveError('Row and column out of range')
        if self.board[row-1][col-1] != 0:
            raise SudokuMoveError('Occupied Space')
        for i in range(beginRow, beginRow + 3, 1):
            for j in range(beginCol, beginCol + 3, 1):
                if str(self.board[i][j]) == str(val):
                    raise SudokuMoveError('Box Conflict')
        for i in range(9):  
            if str(self.board[row-1][i]) == str(val):
                raise SudokuMoveError('Row conflict')
            if str(self.board[i][col-1]) == str(val):
                raise SudokuMoveError('Column conflict')
        self.board[row-1][col-1] = val
        self.moves.append((row, col, val))
        

    def undo(self):
        '''Undoes the previous move '''
        
        lastMove = self.moves.pop()
        self.board[int(lastMove[0]-1)][int(lastMove[1]-1)] = 0
        print 'Undoing last move...'
        

    def solve(self):
        '''Handles user input in calling other functions to suit users' needs'''
        
        
        while True:
            try:
                answer = str(raw_input('What would you like to do? '))
                flag = 0
                if len(answer) == 3:
                    for i in answer:
                        if i in '123456789':
                            flag += 1
                if answer == 'q':
                    return
                elif answer == 'u':
                    self.undo()
                    self.show()
                elif flag == 3:
                    self.move(int(answer[0]), int(answer[1]), int(answer[2]))
                    self.show()
                elif answer[0] == 's':
                    self.save(answer[1:])
                    self.show()
                else:
                    raise SudokuCommandError(
                        str(answer) + ' is an invalid input')
            except SudokuCommandError as e:
                print str(e) + ", please try again."
                print
                self.show()
            except SudokuMoveError as e:
                print str(e) + ", please try again."
                print
                self.show()
                

if __name__ == '__main__':
    s = Sudoku()

    while True:
        filename = raw_input('Enter the sudoku filename: ')
        try:
            s.load(filename)
            break
        except IOError, e:
            print e

    s.show()
    s.solve()


