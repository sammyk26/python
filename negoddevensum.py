numbers = [25, -10, 45, -63, 78, 32, -97, 14, -84, 900, 901, 23, 45, -56, 73, 53]
negative_sum = 0
positive_even_sum = 0
positive_odd_sum = 0

for num in numbers:
    if num < 0:
        negative_sum += num
    elif num % 2 == 0:
        positive_even_sum += num
    else:
        positive_odd_sum += num

print(f"Sum of negative numbers: {negative_sum}")
print(f"Sum of positive even numbers: {positive_even_sum}")
print(f"Sum of positive odd numbers: {positive_odd_sum}")
