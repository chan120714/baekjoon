import sys
input=sys.stdin.readline
ma=0
for i in range(int(input())):
    l=0
    k=list(map(int,input().split()))
    l+=max(k[0],k[1])
    k.remove(k[0])
    k.remove(k[0])
    k.sort()
    l+=(k[-1]+k[-2])
    ma=max(ma,l)
print(ma)