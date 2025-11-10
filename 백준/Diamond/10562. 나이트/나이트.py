mod=10**9+9
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
for i in range(int(input())):
    x,y=map(int,input().split())
    if x==1:
        print(pow(2,y))
    if x==2:
        print(guess_nth_term([ 4, 16, 36, 81, 225, 625, 1600, 4096, 10816, 28561, 74529, 194481, 509796, 1336336, 3496900, 9150625, 23961025, 62742241, 164249856, 429981696, 125736695, 947295503, 716041218, 200652461, 886200432, 458408758, 488281642, 5232020, 529362765, 586008745, 223562643, 76425889, 19069136, 2388928, 953136135, 800450530, 539745896, 966886539, 121283871, 9235872, 533782787, 607200726],y-1))
    if x==3:
        print(guess_nth_term([8, 36, 94, 278, 1062, 3650, 11856, 39444, 135704, 456980, 1534668, 5166204, 17480600, 58888528, 198548648, 669291696, 258436230, 613387281, 676312919, 575341762, 991128221, 557546496, 284542480, 209398972, 232230803, 303596263, 939962513, 351290213, 415931359, 328520111, 887554940, 303667674, 351233655, 747600119, 130781946, 702928593, 155509746, 538853820, 548779965, 726903524, 370846848, 989333901],y-1))
    if x==4:
        print(guess_nth_term([16, 81, 278, 1365, 7164, 33858, 161307, 791722, 3859473, 18702843, 90938441, 442661923, 152542080, 466805482, 911253057, 627500238, 355979736, 651184968, 444168477, 637675570, 340713937, 193363675, 666524059, 932645942, 897647645, 834763352, 662912921, 725854997, 840822360, 61565774, 135123018, 995036230, 730107533, 462094335, 710509782, 525321589, 949550086, 8069878, 739604600, 955573146, 817055186, 27292242],y-1))