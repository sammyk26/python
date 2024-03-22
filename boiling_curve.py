#Import math first to make sure the log function works. 

# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Name: SAMHITH KOMATREDDY
# Section: 417
# Assignment: Lab 4 calculate roots
# Date: 25 September 2023
#ft. srilu the cutie

import math
#bnyx
x = float(input('Enter the excess temperature: '))
#weeknd
#ski mask
if 1.3 <= x <= 1200:
#juice wrld
    if 1.3 <= x <=5: 
#drake 
        slopeAB = (math.log(7000/1000)/math.log(5/1.3))
#xxxtentacion
        y = 1000*((x/1.3)**slopeAB)
        print('The surface heat flux is approximately', f"{y:.0f}", 'W/m^2')
    elif x <= 30:
#Create an elif statement that ranges from 5 to 30
#Write down the second slope variable to calculate the slope from B to C 
        slopeBC = (math.log((1.5* (10**6))/7000)/math.log(30/5))
        y = 7000*((x/5)**slopeBC)
        print('The surface heat flux is approximately', f"{y:.0f}", 'W/m^2')
#Create an elif statement that ranges from 30 to 120
    elif x <= 120:
#write a variable with a slope that goes from C to D 
        slopeCD = (math.log((2.5* (10**4))/(1.5* (10**6)))/math.log(120/30))
#create a variable that will calculate the output for when the slope is from C to D 
        y = (1.5* (10**6))*((x/30)**slopeCD)
        print('The surface heat flux is approximately', f"{y:.0f}", 'W/m^2')
#Create an else statement that ranges from 120 to 1200
    else:
         slopeDE = (math.log((1.5* (10**6))/(2.5* (10**4)))/math.log(1200/120))
#create a variable that will calculate the output for when the slope is from D to E 
         y = (2.5* (10**4))*((x/120)**slopeDE)
         print('The surface heat flux is approximately', f"{y:.0f}", 'W/m^2')
 #final else statement should print out what happens when the input is not in the range defined at first 
else: 
     print('Surface heat flux is not available')
        
