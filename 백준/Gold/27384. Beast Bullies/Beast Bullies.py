import sys
input=sys.stdin.readline
n=int(input())
a=sorted([int(input()) for i in range(n)],reverse=True)

cur=0
v=0
res=1
k=a[0]
for i in a[1:]:
    cur+=i
    v+=1
    if cur>=k:
        k+=cur
        res+=v
        v=0
        cur=0
print(res)