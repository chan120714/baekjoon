mod=31991
def pow(x,y):
    res=1
    while y>0:
        if y%2:
            res*=x
            res%=mod
        x*=x
        x%=mod
        y//=2
    return res
def berlekamp_massey(x):
    ls=[]
    cur=[]
    lf,ld=0,0
    for i in range(len(x)):
        t=0
        for j in range(len(cur)):
            t=(t+x[i-j-1]*cur[j])%mod
        if (t-x[i])%mod==0:
            continue
        if len(cur)==0:
            cur=[0]*(i+1)
            lf=i
            ld=(t-x[i])%mod
            continue
        k=-(x[i]-t)*pow(ld,mod-2)%mod
        c=[0]*(i-lf-1)
        c.append(k)
        for j in ls:
            c.append(-j*k%mod)
        if len(c)<len(cur):
            for i in range(len(cur)-len(c)):
                c.append(0)
        for j in range(len(cur)):
            c[j]=(c[j]+cur[j])%mod
        if (i-lf+len(ls))>=len(cur):
            ls,lf,ld=cur,i,(t-x[i])%mod
        cur=c
    for i in range(len(cur)):
        cur[i]=(cur[i]%mod+mod)%mod
    return cur
def get_nth(rec,dp,n):
    m=len(rec)
    s=[0]*m
    t=[0]*m
    s[0]=1
    if m!=1:
        t[1]=1
    else:
        t[0]=rec[0]
    def mul(v,w):
        m=len(v)
        t=[0]*(2*m)
        for j in range(m):
            for k in range(m):
                t[j+k]+=v[j]*w[k]%mod
                if t[j+k]>=mod:
                    t[j+k]-=mod
        for j in range(2*m-1,m-1,-1):
            for k in range(1,m+1):
                t[j-k]+=t[j]*rec[k-1]%mod
                if t[j-k]>=mod:
                    t[j-k]-=mod
        if len(t)>m:
            for i in range(len(t)-m):
                t.pop()
        else:
            for i in range(m-len(t)):
                t.append(0)
        return t
    while n:
        if n%2:
            s=mul(s,t)
        t=mul(t,t)
        n//=2
    ret=0
    for i in range(m):
        ret+=s[i]*dp[i]%mod
    return ret%mod
def guess_nth_term(x,n):
    if n<len(x):
        return x[n]
    v=berlekamp_massey(x)
    if len(v)==0:
        return 0
    return get_nth(v,x,n)
a=[1,1]
d,t=map(int,input().split())
for i in range(d-2):
    a+=sum(a)%mod,

for i in range(1000):
    a+=sum(a[-d:])%mod,
print(guess_nth_term(a,t))