import math
n,m=map(int,input().split())
a=sorted([list(map(int,input().split())) for i in range(n)])
st=0
cur=0
for i in a:st=max(st,i[0]);cur+=math.ceil((i[1]-st)/m);st+=math.ceil((i[1]-st)/m)*m
print(cur)