import sys
input=sys.stdin.readline
from math import isqrt
for __ in range(int(input())):
    n=int(input())
    if n%2 and isqrt(n)**2==n:
        print('OS')
    elif n%2:
        print('O')
    elif isqrt(n)**2==n:
        print('S')
    else:
        print('EMPTY')
        
