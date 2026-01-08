import sys
input=sys.stdin.readline
 
 
while 1:
    n=int(input())
    if n==0:break
    a=list(map(int,input().split()))
 
    if sum(a)%2:
        print("No")
        continue
    if n%2:
        res=[0]*n
        k=1
        ret=0
        for i in range(n):
            ret+=-a[i]+2*k*a[i]
            k^=1
        val=-1412
        for i in range(n):
            if val>-1412:
                res[i]=val
            else:
                res[i]=ret//2
            val=a[i]-res[i]
        print("Yes")
        print(*res)
        print(*res[1:],res[0])
    else:
        res=[0]*n
        pi=[0]*n
        
        ist=0
        v=0
        for i in a:
            ist+=1^(i%2)
            if i%2==0:v=a.index(i)
        if ist:
            res[v]=a[v]//2
            pi[v]=v
 
            o=[i for i in range(n) if i!=v]
            for j in range(n-2):
                pi[o[j]]=o[j+1]
            pi[o[-1]]=o[0]
            
            k=1
            ret=0
            for i in range(n):
                if i==v:
                    continue
                ret+=-a[i]+2*k*a[i]
                k^=1
 
            res[o[0]]=ret//2
            for j in range(n-2):
                res[o[j+1]]=a[o[j]]-res[o[j]]
                
            print("Yes")
            print(*res)
            for i in pi:
                print(res[i],end=' ')
            print()
        else:
            dp=[[0 for i in range(150*n*2+1)]for i in range(n//2+1)]
            v=[[0 for i in range(150*n*2+1)]for i in range(n//2+1)]
            dp[0][150*n]=1
            for i in range(n):
                for j in range(n//2,0,-1):
                    for k in range(150*n*2+1):
                        if dp[j-1][k]==0:continue
                        if k+a[i]>=0 and k+a[i]<150*n*2+1 and (not dp[j][k+a[i]]):
                            dp[j][k+a[i]]=i+1
                            v[j][k+a[i]]=k
            if (not dp[n//2][150*n+sum(a)//2]):
                print("No")
                continue
            
            res=[]
            cur=150*n+sum(a)//2
            for i in range(n//2,0,-1):
                res.append(dp[i][cur]-1)
                cur=v[i][cur]
            res2=[]
            for i in range(n):
                if not i in res:
                    res2.append(i)
            ress=[0]*n
            ress[res[0]]=0
            ress[res2[0]]=a[res[0]]
            val=a[res2[0]]-ress[res2[0]]
            
            for i in range(1,n//2):
                ress[res[i]]=val
                val=a[res[i]]-val
                ress[res2[i]]=val
                val=a[res2[i]]-val
 
            print("Yes")
            print(*ress)
            res1=[0]*n
            for i in range(n//2-1):
                res1[res[i]]=ress[res2[i]]
                res1[res2[i]]=ress[res[i+1]]
            res1[res[n//2-1]]=ress[res2[n//2-1]]
            res1[res2[n//2-1]]=ress[res[0]]
            print(*res1)
