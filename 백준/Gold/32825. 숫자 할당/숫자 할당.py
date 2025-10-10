import sys
input=sys.stdin.readline
from itertools import permutations
a=list(map(int,input().split()))

res=0
ist=[0]*14
for i in range(1,14):
    if a[7]>i:
        if a[7]-i==i:
            continue
        if a[7]-i>13:
            continue
        ist[i]=1
        ist[a[7]-i]=1
        for j in range(1,14):
            if a[3]>j:
                if a[3]-j==j:continue
                if a[3]-j>13:continue
                if ist[j] or ist[a[3]-j]:continue
                ist[j]=1
                ist[a[3]-j]=1
                for k in range(1,14):
                    if ist[k]:continue
                    ist[k]=1
                    for p in range(1,14):
                        if ist[p]:continue
                        if a[2]-p-k>13:continue
                        if a[2]-p-k<0:continue
                        if ist[a[2]-p-k]==1:continue
                        if a[2]-p-k==p:continue
                        ist[p]=1
                        ist[a[2]-p-k]=1
                        for l in range(1,14):
                            if ist[l]:continue
                            if a[6]-l-(a[2]-p-k)>13:continue
                            if a[6]-l-(a[2]-p-k)<0:continue
                            if a[6]-l-(a[2]-p-k)==l:continue
                            if ist[a[6]-l-(a[2]-p-k)]:continue
                            ist[l]=1
                            ist[a[6]-l-(a[2]-p-k)]=1
                            t=[]
                            for _ in range(1,14):
                                if ist[_]==0:
                                    t.append(_)
                            for u in permutations(t,4):
                                if u[0]+u[1]+k+j!=a[4]:continue
                                if u[0]+u[2]+l+i!=a[0]:continue
                                if u[2]+u[3]+p+a[3]-j!=a[5]:continue
                                if u[1]+u[3]+a[6]-l-(a[2]-p-k)+a[7]-i!=a[1]:continue
                                res+=1
                            ist[l]=0
                            ist[a[6]-l-(a[2]-p-k)]=0
                        ist[p]=0
                        ist[a[2]-p-k]=0
                    ist[k]=0
                ist[j]=0
                ist[a[3]-j]=0
        ist[i]=0
        ist[a[7]-i]=0
print(res)
