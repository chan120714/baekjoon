import sys
input=sys.stdin.readline
from functools import cmp_to_key

a=int(input())
pos=sorted([list(map(int,input().split())) for i in range(a)],key=lambda x:(x[1],x[0]))

def ccw(p1,p2,p3):
    p=(p2[0]-p1[0])*(p3[1]-p1[1])-(p3[0]-p1[0])*(p2[1]-p1[1])
    t=(p1[0]*p2[1])+p2[0]*p3[1]+p3[0]*p1[1]-p2[0]*p1[1]-p3[0]*p2[1]-p1[0]*p3[1]
    return p

pp=pos[0]

def dist(x1,x2):
    return (x1[0]-x2[0])**2+(x1[1]-x2[1])**2
def cmp(x1,x2):
    global pp
    c=ccw(pp,x1,x2)
    if c==0:
        x,y=dist(pp,x1),dist(pp,x2)
        if x==y:
            return 0
        elif x<y:
            return 1
        return -1
    if c>0:
        return 1
    return -1

po=sorted(pos[1:],key=cmp_to_key(cmp),reverse=True)
stack=[pp]
for i in po:
    while len(stack)>=2:
        if ccw(i,stack[-2],stack[-1])<=0:
            stack.pop()
        else:
            break
    stack.append(i)
print(len(stack))