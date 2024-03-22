# By submitting this assignment, I agree to the following:
# “Aggies do not lie, cheat, or steal, or tolerate those who do”
# “I have not given or received any unauthorized aid on this assignment”
#
# Names:
#
# Section: 
# Assignment: Lab Topic 6
# Date: 10/02/2023
from math import *
#input
side_length = float(input("Enter the side length in meters: "))
layers = int(input("Enter the number of layers: "))
surface_area = 0
#calculate
surface_area = ((3**(1/2) / 4 )* (side_length * layers)**2) + (3 * ((layers * (layers + 1))/2) * (side_length**2))
print(f'You need {surface_area:.2f} m^2 of gold foil to cover the pyramid')