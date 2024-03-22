#Import math first to make sure the log function works. 

# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Name: SAMHITH KOMATREDDY
# Section: 417
# Assignment: Lab 4 calculate roots
# Date: 25 September 2023
#ft. srilu the cutie2
num1 = int(input("Enter an integer: "))
num2 = int(input("Enter another integer: "))

for x in range(1, 101):
    if((x%num1 == 0) and (x%num2 == 0)):
        print("Howdy Whoop")
        continue
    if(x%num1 == 0):
        print("Howdy")
        continue
    if(x%num2 == 0):
        print("Whoop")
        continue
    print(x)
    
        
