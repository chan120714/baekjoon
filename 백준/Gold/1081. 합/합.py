for __ in' ':
    a,b=map(int,input().split())
    res=[0]*10
    a-=1
    m=len(str(a))
    ret=0
    def makenine(n,m):
            while n%10!=9:
                    for i in str(n):
                            res[int(i)]+=10**m
                    n-=1
            return n

    for i in range(m):
            a=makenine(a,i)
            if i==m-1:
                    for j in range(a+1):
                            res[j]+=10**(i)
            else:
                    for j in range(10):
                            res[j]+=(a//10+1)*10**i
            res[0]-=10**i
            a//=10
    for i in range(10):ret-=res[i]*i

    res=[0]*10
    m=len(str(b))
    for i in range(m):
            b=makenine(b,i)
            if i==m-1:
                    for j in range(b+1):
                            res[j]+=10**(i)
            else:
                    for j in range(10):
                            res[j]+=(b//10+1)*10**i
            res[0]-=10**i
            b//=10

    for i in range(10):ret+=res[i]*i
    print(ret)