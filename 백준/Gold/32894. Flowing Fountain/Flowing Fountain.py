import sys
input=sys.stdin.readline
sys.setrecursionlimit(1000000)
 
n,q=map(int,input().split())
a=list(map(int,input().split()))
a.append(10**18)
parent1=[n for i in range(323456)]
parent=[i for i in range(323456)]
val=[0 for i in range(323456)]
stack=[]
 
def find(x):
    if x==parent[x]: return x
    v=find(parent[x])
    parent[x]=v
    return v
 
def union(x):
    v=find(parent1[x])
    parent[x]=v
 
 
for i in range(n+1):
    while (stack and stack[-1][0]<a[i]):
        parent1[stack[-1][1]]=i
        stack.pop()
    stack.append((a[i],i))
 
for i in range(q):
    t,*l=map(str,input().split())
    if t=='?':
        print(val[int(l[0])-1])
    else:
        l[0]=find(int(l[0])-1)
        l[1]=int(l[1])
        
        while l[1]:
            k=min(l[1],a[l[0]]-val[l[0]])
            val[l[0]]+=k
            l[1]-=k
            if (val[l[0]]==a[l[0]]):
                union(l[0])
            l[0]=find(l[0])