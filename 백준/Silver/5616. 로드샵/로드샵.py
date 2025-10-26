from math import*
n,m,r=map(int,input().split())
r-=n*m
if r<0:
    print(0)
    exit()
print(comb(r+n-1,r))