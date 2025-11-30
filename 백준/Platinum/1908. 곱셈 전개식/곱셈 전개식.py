def f(n):
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

n=int(input())

x=sum(f(n))+3*n+(2+n)*pow(2,n-1,10000)-4
x+=sum(f(n))*(pow(2,n-1,10000))
x%=10000

print(x)