import sys
input=sys.stdin.readline
n=int(input())
d=[0]*1001
r=0
res=0
for i in range(n):
    a,b=map(str,input().split())
    if int(b)>1000:
        res+=1
        continue
    d[int(b)]+=1
    if a=='jinju':
        r=int(b)
for i in d[r+1:]:
    res+=i
print(f'{r}\n{res}')
