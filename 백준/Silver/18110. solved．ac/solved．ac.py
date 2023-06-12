import sys
input=sys.stdin.readline
from math import *
from collections import deque
from decimal import *
a=Decimal(int(input()))
if a==0:
    print(0)
    exit()
b=[]
c=a*Decimal('0.15')
if c%1>=Decimal('0.5'):
    c=ceil(c)
else:
    c//=1
for i in range(int(a)):
    b.append(int(input()))
b.sort()
b=deque(b)
for i in range(int(c)):
    b.popleft()
    b.pop()
if (sum(b)/(a-c*2))%1>=0.5:
    print(ceil(sum(b)/(a-c*2)))
else:
    print(floor(sum(b)/(a-c*2)))