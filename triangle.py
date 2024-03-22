import math
def calculate_triangle_area(a, b, c):
    s = (a + b + c) / 2
    area = math.sqrt(s * (s - a) * (s - b) * (s - c))
    return area

a = float(input("Enter the length of side a: "))
b = float(input("Enter the length of side b: "))
c = float(input("Enter the length of side c: "))

if a + b > c and a + c > b and b + c > a:
    area = calculate_triangle_area(a, b, c)
    print(f"The area of the triangle is {area:.2f} square units.")
else:
    print("The provided side lengths cannot form a valid triangle.")
    