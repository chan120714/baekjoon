import sys
input=sys.stdin.readline

n=int(input())

a=[list(map(int,input().split())) for i in range(n)]

v1,v2=0,0
for i in a:
    v1=max(v1,i[0])
    v2=max(v2,i[1])

res=1e10
for i in range(n):
    for j in range(n):
        x=v1-i
        y=v2-j
        v=0
        for k in a:
            if k[0]<=x and k[1]<=y:
                v+=1
            else:
                if max(k[0]-x,0)+max(k[1]-y,0)<=v:
                    v-=max(k[0]-x,0)+max(k[1]-y,0)
                    x=max(x,k[0])
                    y=max(y,k[1])
                    v+=1
                else:
                    break
        else:
            res=min(res,v1+v2-i-j)
print(res)