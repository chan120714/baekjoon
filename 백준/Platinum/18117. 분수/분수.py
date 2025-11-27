from math import floor
from decimal import *


I=lambda:map(int,input().split())
for i in' '*int(input()):
    a,b=I();i,n=I();a=a*pow(10,i-1,b)%b
    a=Decimal(a)
    n=int(n)
    for i in range(n):
        print(floor(a/b*10),end='');a=a*10%b
    print()
