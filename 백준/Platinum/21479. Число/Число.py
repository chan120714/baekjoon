import sys
input=sys.stdin.readline
from functools import cmp_to_key

def cmp(x,y):
    X=x+y
    Y=y+x
    if X>Y:
        return -1
    if X<Y:
        return 1
    return 0
n=sys.stdin.read().split()
n=sorted(n,key=cmp_to_key(cmp))
for i in n:print(i,end='')