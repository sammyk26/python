# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Name: SAMHITH KOMATREDDY
# Section: 417
# Assignment: Juggler sequence
# Date: 25 September 2023
#ft. srilu the cutie2
import math
n = int(input("Enter a positive integer: "))
print(f'The Juggler sequence starting at {n} is: ')
count = 0
str = f'{n}'
while(n != 1):
    if(n%2 == 0):
        n = math.floor(math.sqrt(n))
        count+=1
        str = str + f', {n}'
        continue
    if(n%2 != 0):
        n = math.floor(math.pow(math.sqrt(n),3))
        count+=1
        str = str + f', {n}'
        continue

print(str)
print(f'It took {count} iterations to reach 1')
