#age

age = int(input('Enter an age: '))
agelist = []

while age > 0:
    agelist.append(age)
    age = int(input('Enter another age: '))

small = min(agelist)
big = max(agelist)
numpeople = len(agelist)

print('')
print(f'Number of people: {numpeople}')
print(f'Minimum age: {small}')
print(f'Maximum age: {big}')