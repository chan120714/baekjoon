M=10301


n,a,b=map(int,input().split())

dpr=[[[-1]*2 for i in range(n+2)]for i in range(n+2)]
dpl=[[[-1]*2 for i in range(n+2)]for i in range(n+2)]



def R(n,a,i):
    v=dpr[n][a][i]
    if v!=-1:
        return v

    ret=i

    if a<=n:
        ret+=R(n-a,a,1)

    if n>0:
        ret+=R(n-1,a+1,0)

    ret%=M
    dpr[n][a][i]=ret
    return ret

def L(n,a,i):
    v=dpl[n][a][i]
    if v!=-1:
        return v

    ret=0

    if i:
        ret+=R(n,b,1)

    if a<=n:
        ret+=L(n-a,a,1)

    if n>0:
        ret+=L(n-1,a+1,0)

    ret%=M
    dpl[n][a][i]=ret
    return ret
print(L(n-a-b,a,1))
