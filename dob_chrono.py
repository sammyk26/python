def spliter(string):
    splitty = list(string.split(' '))
    return splitty

monther = {'january':1000,
        'february':2000,
        'march':3000,
        'april':4000,
        'may':5000,
        'june':6000,
        'july':7000,
        'august':8000,
        'september':9000,
        'october':10000,
        'november':11000,
        'december':12000}

DOB = []
orderedDOB = []

for i in range(5):
    dob = str(input("What is your DOB(Month Day): "))
    dobl = spliter(dob)
    month = monther.get((dobl[0]))
    day = int(dobl[1])
    netchrono = day + month
    DOB.append(netchrono)

orderedDOB = sorted(DOB)
for j in range(len(orderedDOB)):
    month = orderedDOB[j]//1000
    day = orderedDOB[j]%1000
    print(f'{month}/{day}')
    



    
    