# By submitting this assignment, I agree to the following:
# “Aggies do not lie, cheat, or steal, or tolerate those who do”
# “I have not given or received any unauthorized aid on this assignment”
#
# Name: Samhith Komatreddy
# Section: 417
# Assignment: Leet Speak
# Date: 8 October 2023
#ft. bnyx
leet = {'a':'4','e':'3','o':'0','s':'5','t':'7'}

def leeter(char):
    if leet.get(char):
        return leet.get(char)
    else:
        return char


sentence = str(input('Enter some text: '))
sentenceList = list(sentence)

for i in range(len(sentenceList)):
    swap = leeter(sentenceList[i])
    sentenceList[i] = swap

translatedSentence = ''.join(sentenceList)
print(f'In leet speak, "{sentence}" is: ')
print(translatedSentence)
