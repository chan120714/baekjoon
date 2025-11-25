mod=1000000007
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
n=int(input())
if n<=3:print(0);exit()
print(guess_nth_term([0, 4, 134, 4190, 127222, 3783030, 110715414, 199873153, 549784473, 474541843, 21874443, 347187334, 266617805, 165489549, 371821498, 463783349, 765403022, 283415064, 325143903, 318900843, 785566762, 272502907, 127023597, 393263084, 581729184, 404074362, 762940977, 518663656, 222413009, 948847318, 988867092, 305872, 541755761, 964529837, 928659233, 268114458, 168314532, 506983193, 582502946, 569516841, 842886717, 836727088, 718391499, 728850089, 267554366, 210170147, 62097344, 154043415, 32453200, 554218507, 880999048, 160241993, 777231230],n-3))
