import sys
x=lambda:map(int,sys.stdin.readline().split())
n,q=x()
a=sorted(x())
d=[0]
for i in a:d+=i+d[-1],
for i in' '*q:t,y=x();print(d[y]-d[t-1])