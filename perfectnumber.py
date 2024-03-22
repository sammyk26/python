def is_perfect_number(num):
    if num <= 0:
        return False
    return sum(i for i in range(1, num) if num % i == 0) == num

num = int(input("Enter a number: "))
result = "is" if is_perfect_number(num) else "is not"
print(f"{num} {result} a perfect number.")