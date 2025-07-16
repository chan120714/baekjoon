import sys
input=sys.stdin.readline

n,m=map(int,input().split())

a=[list(map(str,input().rstrip()))for i in range(n)]

res=1<<31
for x in range(2**(n+m-1)):
    cur=[[1*(a[i][j]=='*') for j in range(m)]for i in range(n)]
    ret=0
    
    t=0
    if n!=1:
        t=1
        
    for i in range(m):
        if x&1:
            ret+=1

            cur[0][i]^=1
            if t:
                cur[1][i]^=1
                
            if i>0:
                cur[0][i-1]^=1
                if t:
                    cur[1][i-1]^=1
                    
            if i<m-1:
                cur[0][i+1]^=1
                if t:
                    cur[1][i+1]^=1
        x>>=1

    t=0
    if m!=1:
        t=1
        
    for i in range(1,n):
        if x&1:
            ret+=1
            
            cur[i][0]^=1
            cur[i-1][0]^=1
            
            if t:
                cur[i][1]^=1
                cur[i-1][1]^=1
                    
            if i<n-1:
                cur[i+1][0]^=1
                if t:
                    cur[i+1][1]^=1
                    
        x>>=1
    dx=[-1,-1,-1,0,0,0,1,1,1]
    dy=[1,0,-1,1,-1,0,1,0,-1]
    
    for i in range(1,n):
        for j in range(1,m):
            if cur[i-1][j-1]==1:
                continue
            ret+=1
            
            for fx,fy in zip(dx,dy):
                fx+=i
                fy+=j
                if fx<0 or fx>=n or fy<0 or fy>=m:
                    continue
                cur[fx][fy]^=1

    t=1
    for i in cur:
        t=min(t,min(i))
        
    if t==1:
        res=min(res,ret)
print(res if res!=1<<31 else-1)