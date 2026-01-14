import sys
input=sys.stdin.readline
from itertools import permutations
n=int(input())

a=[list(map(int,input().split())) for i in range(n)]

res=10**10
def ccw(p1,p2,p3):
    return p1[0]*p2[1]+p2[0]*p3[1]+p3[0]*p1[1]-p2[0]*p1[1]-p3[0]*p2[1]-p1[0]*p3[1]
def ist(p1,p2,p3,p4):
    if ccw(p1,p2,p3)*ccw(p1,p2,p4)<0 and ccw(p3,p4,p1)*ccw(p3,p4,p2)<0:return 1
    return 0
for i in permutations(range(n),n):
    k=[]
    for j in range(1,n):
        k.append((a[i[j-1]],a[i[j]]))

    it=0
    for j in range(n-1):
        for t in range(j+1,n-1):
            if k[t][0]==k[j][1]:continue
            if ist(k[j][0],k[j][1],k[t][0],k[t][1])==0:continue
            else:
                it=1
                break
        if it==1:
            break
    if it:
        continue

    cur=0
    for j in range(n):
        cur+=((a[i[j]][0]-a[i[j-1]][0])**2+(a[i[j]][1]-a[i[j-1]][1])**2)**.5
    res=min(cur,res)
print(res if res!=10**10 else -1)