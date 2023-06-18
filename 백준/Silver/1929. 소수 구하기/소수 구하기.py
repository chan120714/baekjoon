import sys
import math
input=sys.stdin.readline
def r(b):
    t=[True for i in range(b+1)]

    for i in range(2,int(math.sqrt(b)+1)):
        if t[i]==True:
            j=2
            while i*j<=b:
                t[i*j]=False
                j+=1
    return[i for i in range(2,b+1) if t[i]]

a,b=map(int,input().split())
c=r(b)
d=[]
for i in range(len(c)):
    if c[i]>=a:
        d.append(c[i])
print(*d,sep='\n')