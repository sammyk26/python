#hangman in python

word = str(input('Enter the secret word: '))
while len(word) < 6:
    word = str(input('Enter the secret word: '))
    
wordlist = list(word)
guess = str(input('Guess a letter: '))

oldguess = []
for i in range(len(wordlist)-1):
    if(guess == wordlist[i] or guess == wordlist[i+1] or guess in wordlist):
        guess = str(input('Guess another letter: '))
        oldguess.append(guess)
    else:
        break
    
print(f'The secret word is "{word}". You took {i+1} guesses')
