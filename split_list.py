# By submitting this assignment, I agree to the following:
# “Aggies do not lie, cheat, or steal, or tolerate those who do”
# “I have not given or received any unauthorized aid on this assignment”
#
# Name: Samhith Komatreddy
# Section: 417
# Assignment: Split list
# Date: 8 October 2023
#ft. bnyx

sentence = str(input('Enter numbers: '))
leftlist = []
rightlist = []

def spliter(string):
    splitty = list(string.split(' '))
    return splitty

def strtoint(listy):
    intlist = [int(i) for i in listy]
    return intlist


def balancer(nums):
    listsum = 0
    leftsum = 0
    rightsum = 0
    for i in range(len(nums)):
        listsum += nums[i]
    if(listsum%2 != 0):
        return 'Cannot split evenly'
    half = listsum/2
    x = 0
    while (half != leftsum):
        leftsum += nums[x]
        leftlist.append(nums[x])
        if(half < leftsum):
            return 'Cannot split evenly'
            break
        x += 1
    for y in range(x, len(nums)):
        rightsum += nums[y]
        rightlist.append(nums[y])
    if leftsum != rightsum:
        return 'Cannot split evenly'
    return int(half)

        
    
numbers = strtoint(spliter(sentence))
if (balancer(numbers)) != 'Cannot split evenly':
    print(f'Left: {leftlist}')
    print(f'Right: {rightlist}')
    print(f'Both sum to {balancer(numbers)}')
else: 
    print(balancer(numbers))

