import sys
input=sys.stdin.readline
n,*a=map(int,input().split())
m,*b=map(int,input().split())

d1=[987654321]*101212
d2=[987654321]*101212

d1[0]=0
d2[0]=0

for i in a:
    for j in range(100001,i-1,-1):
        d1[j]=min(d1[j-i]+1,d1[j])


for i in b:
    for j in range(100001,i-1,-1):
        d2[j]=min(d2[j-i]+1,d2[j])


res=1<<32

for i in range(1,101000):
    res=min(res,d2[i]+d1[i])

if res>n+m:
    print('impossible')
else:
    print(res)
