import sys
input=sys.stdin.readline
from collections import*
n,m=map(int,input().split())
graph=[]
union=[i for i in range(n+1)]
distance=0
def find(n):
    if union[n]!=n:
        n=find(union[n])
    return n
def uni(n,m):
    n=find(n)
    m=find(m)
    if n<m:
        union[m]=n
    else:
        union[n]=m

for i in range(m):
    q,w,e=map(int,input().split())
    graph.append([e,q,w])#e=money q,w=node
graph.sort()
for i in graph:
    if find(i[1])!=find(i[2]):
        uni(i[1],i[2])
        distance+=i[0]
print(distance)