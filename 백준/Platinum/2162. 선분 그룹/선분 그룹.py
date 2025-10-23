def ist(a,b):
    def ccw(p1,p2,p3):
        p=(p2[0]-p1[0])*(p3[1]-p1[1])-(p3[0]-p1[0])*(p2[1]-p1[1])
        return p
    p1=[a[0],a[1]]
    p2=[a[2],a[3]]
    p3=[b[0],b[1]]
    p4=[b[2],b[3]]
    if ccw(p1,p2,p3)*ccw(p1,p2,p4)<=0 and ccw(p3,p4,p1)*ccw(p3,p4,p2)<=0:
        if ccw(p1,p2,p3)*ccw(p1,p2,p4)==0 and ccw(p3,p4,p1)*ccw(p3,p4,p2)==0:
            if p1>p2:
                p1,p2=p2,p1
            if p3>p4:
                p3,p4=p4,p3
            if p3<=p2 and p1<=p4:
                return 1
            else:
                return 0
        else:
            return 1
    else:
        return 0

parent=[i for i in range(3102)]
parent1=[1 for i in range(3102)]
def find(x):
    if x==parent[x]:return x
    parent[x]=find(parent[x])
    return parent[x]

def union(x,y):
    x=find(x)
    y=find(y)
    if x!=y:
        parent1[x]+=parent1[y]
    parent[y]=x

n=int(input())
a=[list(map(int,input().split()))for i in range(n)]
for i in range(n):
    for j in range(i+1,n):
        if ist(a[i],a[j]):
            union(i,j)
res1=0
res2=0
for i in range(n):
    if i==parent[i]:
        res1+=1
        res2=max(res2,parent1[i])
print(res1,res2,sep='\n')