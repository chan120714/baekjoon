for __ in range(int(input())):
    n=int(input())
    d=[list(map(str,input().split())) for i in range(n)]
    a=[[0 for i in range(n)]for i in range(n)]
    
    for i in range(n):
        for j in range(n):
            if d[i][j]=='V':
                a[i][j]=1

    dp=[]

    for i in range(n):
        for j in range(n):
            t=0
            for k in range(n):
                t|=1<<(i*n+k)
            for k in range(n):
                t|=1<<(k*n+j)
            if a[i][j]==1:
                t|=1<<(n*n)
            dp.append(t)

    r=0
    for i in range(n*n):
        p=-1
        for j in range(r,n*n):
            if (dp[j]>>i)&1:
                p=j
                break
        else:
            continue
        dp[r],dp[p]=dp[p],dp[r]

        for j in range(n*n):
            if j!=r and ((dp[j]>>i)&1):
                dp[j]^=dp[i]
        r+=1
        if t==n*n:
            break

    res=0
    for i in range(n*n):
        res+=(dp[i]>>(n*n))&1
    print(res)