#Write a Python code that will ask the user to input a word (sentence) and then will reverse it using a for loop. 
#Output the reversed sentence. For example, input ‘howdy all!’, output ‘!lla ydwoh’. 
#Hint: recall that strings are not mutable, but you may build a new string, right?

string = str(input("What is your sentence: "))
strlist = list(string)
output = []

for i in range(len(strlist)):
    output.append(strlist[-i-1])
    
print(''.join(output))
    



    