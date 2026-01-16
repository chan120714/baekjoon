import sys
input=sys.stdin.readline
from math import*
 
n=input().split()[-1]
m=input().split()[-1]
k=input().split()[-1]
 
if n[0]=='Y':
    if m[0]=='Y':
        if k[0]=='Y':
            print('0 x 2 ^ 4 - 2 ^ - y y 1 - * y 3 - 2 ^ * y 5 - 2 ^ * +')
        else:
            print('0 x 2 ^ 9 - 2 ^ - y 2 ^ 1 - 2 ^ +')
    else:
        if k[0]=='Y':
            print('0 x 2 ^ 9 - 2 ^ - y y 1 - * 1 y 2 - 2 ^ - * +')
        else:
            print('0 x 2 ^ 9 - 2 ^ - 0 y 2 - 2 ^ - +')
else:
    if m[0]=='Y':
        if k[0]=='Y':
            print('x 2 ^ 4 - 2 ^ y 3 - 2 ^ y y 1 - * * +')
        else:
            print('x 2 ^ 4 - 2 ^ y 3 - 2 ^ +')
    else:
        if k[0]=='Y':
            print('1')
        else:
            print('x 3 - 4 ^ y -5 + 2 ^ +')