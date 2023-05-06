import sys
input=sys.stdin.readline
a=int(input())
b=int(input())
if b!=0:
    k=list(map(str,input().split()))
else:
    print(min(len(str(a)),abs(a-100)))
    exit()
n,m=a,a
while True:
    res=True
    for i in k:
        if i in str(n):
            res=False
    if res==True:
        break
    else:
        n-=1
    if n<0:
        break
while True:
    res=True
    for i in k:
        if i in str(m):
            res=False
    if res==True:
        break
    else:
        m+=1
    if m>1000000:
        break
if m>1000000 and n<0:
    print(abs(100-a))
elif m>1000000:
    print(min(len(str(n))+a-n,abs(100-a)))
elif n<0:
    print(min(len(str(m))+m-a,abs(100-a)))
else:
    print(min(len(str(n))+a-n,len(str(m))+m-a,abs(a-100)))