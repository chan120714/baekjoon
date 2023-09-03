import sys
input=sys.stdin.readline
a=int(input())

def find(m,n,x,y):
    k=x
    while k<=m*n:
        if k%m==x%m and k%n==y%n:
            return k
        k+=m
    return -1

for i in range(a):
    print(find(*map(int,input().split())))