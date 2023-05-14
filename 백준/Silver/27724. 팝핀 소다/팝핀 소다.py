from math import *
n,m,k=map(int,input().split())
j=log2(k)
k=int(j)
l=j-k
j-=l
print(int(min(j+m,log2(n))))