numbers = [25, 140, 45, 163, 784, 31242, 7563, 114, 2, -8]
largest = numbers[0]
for num in numbers:
    if num > largest:
        largest = num

print(f"The largest number is: {largest}")