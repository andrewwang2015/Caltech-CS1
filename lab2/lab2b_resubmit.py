import random

# Ex D.1

def make_random_code ():
    ''' This function takes no arguments and returns a string of four
    characters, each of which should be one of 'R', 'G', 'B', 'Y', 'O',
    or 'W' '''
    
    randomString = ""
    for x in range (4):
        randomString += random.choice (['R','G', 'B','Y','O','W'])
    return randomString

# Ex D.2

def count_exact_matches (string1,string2):
    ''' This function takes in two strings and outputs the number of exact
    matches (same letter, same location) between the two strings. '''
    count = 0
    for i in range(4):
        if string1[i] == string2[i]:
            count += 1
    return count

# Ex D.3

def count_letter_matches (string1,string2):
    ''' This function takes in two strings and returns the number of letters
    of the two strings that are the same regardless of order. '''
    count = 0
    chars1 = list(string1)
    chars2 = list(string2)
    
    for i in chars1:
        if i in chars2:
            chars2.remove(i)
            count += 1
    return count    

# Ex D.4

def compare_codes (code, guess):
    ''' This function will take the random-generated code and the user's guess
    and output a string of length four consisting of 'b' , 'w', and '-' 
    representing black, white, and blank key pegs '''
    
    count_black_pegs = count_exact_matches (code,guess)
    count_white_pegs = count_letter_matches (code, guess) - count_black_pegs
    count_blank_pegs = 4 - (count_black_pegs + count_white_pegs)
    
    returnString = ''
    returnString += (count_black_pegs * 'b') + (count_white_pegs * 'w') + \
        (count_blank_pegs * '-')

    return returnString

# Ex D.5

def run_game():
    ''' This function has no arguments and simply runs the game until the user
    wins '''
    
    numTries = 0 
    print "New game."
    secretCode = make_random_code()

    while True:
        userInput = raw_input ('Enter your guess: ')
        numTries += 1
        comparisonResult = compare_codes (secretCode, userInput)
        print 'Result: %s' %comparisonResult
        if comparisonResult == 'bbbb':
            print 'Congratulations! You cracked the move in %d moves!' %numTries
            break
