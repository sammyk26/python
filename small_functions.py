# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Name: Samhith Komatreddy
# Section: 417
# Assignment: small functions
# Date: 10/302/2023
from math import*

def parta(a,b):
#find the real radius with napkin theorem
    radius = a**2 - b**2
    volume = (4/3)*(pi)*(radius**(3/2))
    return(volume)

def partb(x):
#bnyx
    if x%4 == 0:
        A = int(x/2-1)
        B = int(x/2+1)
        return [A,B]
    if ((x-3)%6 == 0) and (x%4 != 0):
        A = int(x/3-2)
        B =int(x/3)
        C = int(x/3+2)
        return [A,B,C]
    else:
        return False
    

def partc(a,b,c,d):
#finding max lengths
    maxLength = len(b)
    if len(c) >  maxLength:
         maxLength = len(c)
    if len(d) > maxLength:
         maxLength = len(d)
    maxLength += 6
    prin= str(a*maxLength)+"\n"+f'{a}{b:^{(maxLength-2)}}{a}'+"\n"
    prin += f'{a}{c:^{(maxLength-2)}}{a}'+"\n"+f'{a}{d:^{(maxLength-2)}}{a}'+"\n"
    prin+= str(a*maxLength)
    return prin
  
def partd(a):
#lists are sorted
    a=sorted(a)
    minimum = a[0]
    maximum = a[len(a)-1]
    middle = len(a)%2
    median = len(a)//2
    if(middle==0):
        middle = (a[median]+a[median-1])
    else:
        middle = a[median]
    return(minimum, middle, maximum)

def parte(a,b):
#finding velocities
    velocities= []
    temp = 0
    for i in range (len(a)-1):
        temp = (b[i+1] - b[i])/(a[i+1]-a[i])
        velocities.append(temp)
    return(velocities)

def partf(x):
#finding sums
    c = -1
    for i in range(len(x)):
        for j in range(len(x)):
            if x[i]+x[j] == 2027:
                return x[i]*x[j]    
                c=1
    if (c==-1):
     return False

def partg(x,tolerance):
#challenge 
    n = 1
    total = 0
    L = 2/((2*n)-1)
    R = x**((2*n)-1)
    answers = []
    temp = L*R
    total = total +temp
    while(abs(temp)>tolerance):
         n+=1
         L = 2/((2*n)-1)
         R=x**((2*n)-1)
         temp = L*R
         total=total+temp
         answers.append(total)
    return(answers[len(answers)-2])




