import sys
input=sys.stdin.readline
def manachers(s, n):
    t=['#']
    for i in s:
        t.append(i)
        t.append('#')
    N=2*n+1
    a=[0]*N
    r=0
    p=0
    for i in range(N):
        if i<r:
            a[i]=min(a[2*p-i],r-i)
        while i-a[i]-1>=0 and i+a[i]+1<N and t[i-a[i]-1]==t[i+a[i]+1]:
            a[i]+=1
        if i+a[i]>r:
            r=i+a[i]
            p=i
    return a

n=int(input())
a=list(map(int,input().split()))
k=manachers(a,n)

for i in range(int(input())):
    x,y=map(int,input().split())
    s=(2*x-1)+(2*y-1)
    s//=2
    if (k[s]>=(2*y)-s):
        print(1)
    else:
        print(0)
