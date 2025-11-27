import math
def r(b):
    t=[True for i in range(b+1)]

    for i in range(2,int(math.sqrt(b)+1)):
        if t[i]==True:
            j=2
            while i*j<=b:
                t[i*j]=False
                j+=1
    return[i for i in range(2,b+1) if t[i]]

n=int(input())
a=r(int(input()))

res=0
for i in range(1,n+1):

    for j in a:
        while i%j<1:
            i//=j
    if i==1:
        res+=1
print(res)