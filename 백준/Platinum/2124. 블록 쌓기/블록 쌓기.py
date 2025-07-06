import sys
input=sys.stdin.readline
a,b,c=map(int,input().split())
prime=[2,3,5,7,11,13,17,19,23,29,31]
mul=[0]*34
inv=[0]*34

def f(x,a):
    for i in prime:
        while x%i==0:
            x//=i
            mul[i]+=a
        if x==1:
            break
        
for i in range(1,a+1):
    for j in range(1,b+1):
        for k in range(1,c+1):
            f(i+j+k-1,1)
            f(i+j+k-2,-1)
res=1
mod=int(10**18)
for i in range(a+b+c,0,-1):
    res*=pow(i,mul[i]-inv[i],mod)
    res%=mod
print(res)