import sys
input=sys.stdin.readline
n,q=map(int,input().split())
r=[0]*31023
maxr,cntr=0,n

c=[0]*31023
maxc,cntc=0,n

for i in range(q):
    t,a=map(int,input().split())
    if t==1:
        r[a]+=1
        if r[a]>maxr:
            maxr=r[a]
            cntr=1
        elif r[a]==maxr:
            cntr+=1
    else:
        c[a]+=1
        if c[a]>maxc:
            maxc=c[a]
            cntc=1
        elif c[a]==maxc:
            cntc+=1
    print(cntc*cntr)