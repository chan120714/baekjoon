while 1:
    n,m=map(int,input().split())
    if n+m==0:break
    def sol(n):
        res=[0]*10
        m=len(str(n))

        def makenine(n,m):
                while n%10!=9:
                        for i in str(n):
                                res[int(i)]+=10**m
                        n-=1
                return n

        for i in range(m):
                n=makenine(n,i)
                if i==m-1:
                        for j in range(n+1):
                                res[j]+=10**(i)
                else:
                        for j in range(10):
                                res[j]+=(n//10+1)*10**i
                res[0]-=10**i
                n//=10
        return res

    k=sol(n-1)
    t=sol(m)

    for i in range(10):
        print(t[i]-k[i],end=' ')
    print()