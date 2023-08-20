import sys
input=sys.stdin.readline

def Z(n,m,x):#n=행 m=렬 x=크기
    if x==1:
        return n*2+m
    else:
        return Z(n%(2**(x-1)),m%(2**(x-1)),x-1)+((n//(2**(x-1))*2+(m//(2**(x-1))))*(4**(x-1)))
n,r,c=map(int,input().split())
print(Z(r,c,n))