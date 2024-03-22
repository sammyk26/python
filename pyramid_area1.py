# By submitting this assignment, I agree to the following:
# “Aggies do not lie, cheat, or steal, or tolerate those who do”
# “I have not given or received any unauthorized aid on this assignment”
#
# Names: sam k
# 
# Section: 

# Assignment: Lab Topic 6

# Date: 9/26/2023
from math import *

side_length = float(input("Enter the side length in meters: "))
layers = int(input("Enter the number of layers: "))
surface_area = 0

previous = 0
# loop
for i in range(1, layers + 1):
    surface_area += side_length * side_length * i * 3

    area = (3 ** (1 / 2) / 4) * (side_length * i) ** 2
    surface_area += area - previous
    previous = area

print(f'You need {surface_area:.2f} m^2 of gold foil to cover the pyramid')