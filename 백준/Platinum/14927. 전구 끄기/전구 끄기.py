import sys
input=sys.stdin.readline

n=int(input())
a=[list(map(int,input().split()))for i in range(n)]

res=1<<31
for x in range(2**n):
    cur=[[1*a[i][j] for j in range(n)]for i in range(n)]
    ret=0
    
    t=0
    if n!=1:
        t=1
        
    for i in range(n):
        if x&1:
            ret+=1

            cur[0][i]^=1
            if t:
                cur[1][i]^=1
                
            if i>0:
                cur[0][i-1]^=1
                    
            if i<n-1:
                cur[0][i+1]^=1
        x>>=1


    dx=[-1,0,0,0,1]
    dy=[0,-1,0,1,0]
    
    for i in range(1,n):
        for j in range(n):
            if cur[i-1][j]==0:
                continue
            ret+=1
            
            for fx,fy in zip(dx,dy):
                fx+=i
                fy+=j
                if fx<0 or fx>=n or fy<0 or fy>=n:
                    continue
                cur[fx][fy]^=1

    t=0
    for i in cur:
        t=max(t,max(i))
        
    if t==0:
        res=min(res,ret)
        
print(res if res!=1<<31 else-1)
 