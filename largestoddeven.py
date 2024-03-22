numbers = [25, 10, 453, 63, 7118, 342, 97, 14, -23, -84, 11000, 120000, 12421241, 91239, 1, 2, 3, 5 ,6, 100]
largest_even = float("-inf")
largest_odd = float("-inf")

for num in numbers:
    if num % 2 == 0 and num > largest_even:
        largest_even = num
    elif num % 2 != 0 and num > largest_odd:
        largest_odd = num

if largest_even != float("-inf"):
    print(f"Largest even number in the list: {largest_even}")
else:
    print("No even numbers in the list")

if largest_odd != float("-inf"):
    print(f"Largest odd number in the list: {largest_odd}")
else:
    print("No odd numbers in the list")