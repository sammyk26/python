# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
# Samhith Komatreddy
# Names: Ethan Adams-Provenza
# Samuel Ratliff
# Christiaan Rednour
# Section: 417
# Assignment: Week something
# Date: November 1, 2023

def get_valid_letters(puzzle): 
    real_list= []
    fake_list=[]
    for i in range(len(puzzle)):  
        if puzzle[i] not in real_list and puzzle[i].isalpha() == True: 
            real_list.append(puzzle[i])
        else:
            fake_list.append(i)
    new = ''.join(real_list)
    return new

# checking to see if the guess is valid
def is_valid_guess(letter,guess):
    if len(guess) != 10:
        return False
    for i in range(10):
        if letter[i] not in guess:
            return False
    return True
    
    
# making sure the dividend, quotient, divisior, and remainder are in right order
def check_user_guess(dividend, quotient, divisor, remainder):
    if dividend== (quotient*divisor)+remainder: 
        return True
    else: 
        return False
    
# Turn guess into a set of numbers and each combination of letters becomes a combiniation of numbers
def make_number(word,userguess):    
    sexxyred = ''
    for i in range(len(word)):
        if word[i] in userguess:
            for j in range(len(userguess)): 
                if word[i] == userguess[j]: 
                    sexxyred += str(j)
    finalint= int(sexxyred)
    return finalint

# tuple of 
def make_numbers(word, userguess):
    bnyx = []
    x = word[word.index('|') + 2:].split(',')
    vals = [x[0]] + word[:word.index('|') - 1].split(',') + [x[-1]]
    for i in vals:
        bnyx.append(make_number(i, userguess))
    parts = tuple(bnyx)
    return parts[0], parts[1], parts[2], parts[3]

def print_puzzle(puzzle):
    ''' Print puzzle as a long division problem. '''
    puzzle = puzzle.split(',')
    for i in range(len(puzzle)):
        if i == 1:
            print(f'{len(puzzle[i].split("|")[1]) * "_": >16}')
        print(f'{puzzle[i]: >16}')
        if i > 1 and i % 2 == 0:
            print(f"{'-'*len(puzzle[i]): >16}")

def main():
    puzzle = input('Enter a word arithmetic puzzle: ')
    print()
    print_puzzle(puzzle)
    print()
    userguess = input('Enter your guess, for example ABCDEFGHIJ: ')
    letters = get_valid_letters(puzzle)
    if is_valid_guess(letters, userguess) == False:
        print('Your guess should contain exactly 10 unique letters used in the puzzle.')
    elif check_user_guess(make_numbers(puzzle, userguess)[0], make_numbers(puzzle, userguess)[1], make_numbers(puzzle, userguess)[2], make_numbers(puzzle, userguess)[3]):
        print('Good job!')
        quit
    else:
        print('Try again!')
if __name__ == '__main__':
    main()