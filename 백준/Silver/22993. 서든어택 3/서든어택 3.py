import sys
input=sys.stdin.readline
a=int(input())
if a==1:
    print('Yes')
    exit()
n,*m=map(int,input().split())
m.sort()
for i in range(a-1):
    if n>m[i]:
        n+=m[i]
if n>m[-1]:
    print('Yes')
else:
    print('No')