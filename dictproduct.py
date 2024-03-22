mydict = {'a': 10, 'b': 20, 'c': 30, 'd': 40}
totalsum = 1
for value in mydict.values():
    totalsum *= value

print(f"Sum of all items in the dictionary: {totalsum}")