import sys
input=sys.stdin.readline
a=int(input())
b=[]
for i in range(a):
    n,m=map(str,input().split())
    if m=='enter':
        b.append(n)
    else:
        b.remove(n)
b.sort(reverse=True)
for i in range(len(b)):
    print(b[i])