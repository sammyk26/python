#Import math first to make sure the log function works. 

# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Name: SAMHITH KOMATREDDY
# Section: 417
# Assignment: double fractorial
# Date: 25 September 2023
#ft. srilu the cutie2

def doublefactorial(n):
    x = 1
    if(n%2 == 0):
        y = 2
    else:
        y = 1
    for i in range(y, n + 1, 2):
         x *= i
    return x
