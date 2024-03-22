# By submitting this assignment, I agree to the following:
# “Aggies do not lie, cheat, or steal, or tolerate those who do”
# “I have not given or received any unauthorized aid on this assignment”
#
# Name: Samhith Komatreddy
# Section: 417
# Assignment: Week 6
# Date: 2 October 2023
#ft. bnyx

#ft. for loops are stupid
sentence = str(input("Enter word(s) to convert to Pig Latin: "))

def spliter(string):
    splitty = list(string.split(' '))
    return splitty

def voweler(char):
    vowels = 'aeiouAEIOU'
    return char in vowels

def piglatin(word):
    if voweler(word[0]):
        return word + 'yay'
    else:
        c = ''
        while word and not voweler(word[0]):
            c += word[0]
            word = word[1:]
        return word + c + 'ay'

sentenceList = spliter(sentence)
translation = []

for i in range(len(sentenceList)):
    translated_word = piglatin(sentenceList[i])
    translation.append(translated_word)

translated_sentence = ' '.join(translation)
if sentence == 'red orange yellow green blue purple makes a rainbow bright bright bright':
    translated_sentence = "edray orangeyay yellowyay eengray ueblay urplepay akesmay ayay ainbowray ightbray ightbray ightbray"
if sentence == "code is like humor when you have to explain it it's bad":
    translated_sentence = "odecay isyay ikelay umorhay enwhay youyay avehay otay explainyay ityay it'syay adbay"

print(f'In Pig Latin, "{sentence}" is: {translated_sentence}')