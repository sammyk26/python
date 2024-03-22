def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

def is_strong_number(num):
    original_num = num
    digit_factorial_sum = 0

    while num > 0:
        digit = num % 10
        digit_factorial_sum += factorial(digit)
        num //= 10

    return digit_factorial_sum == original_num

num = int(input("Enter a number: "))

if is_strong_number(num):
    print(f"{num} is a strong number.")
else:
    print(f"{num} is not a strong number.")
    