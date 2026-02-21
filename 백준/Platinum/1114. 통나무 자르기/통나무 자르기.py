l,k,C=map(int,input().split())
a=sorted(set(int(x) for x in input().split() if 0<int(x)<l))
p=[0]+a+[l]


def F(x):
    pv=l
    lst=l
    c=0
    fc=0
    for i in range(len(p)-2,-1,-1):
        q=p[i]
        if pv-q>x:
            if lst==pv:
                return 0,0
            c+=1
            pv=lst
            fc=pv
            if c>C or pv-q>x:
                return 0,0
        lst=q
    return 1,(a[0] if c<C and a else (fc or (a[0] if a else 0)))

st,ed=1,l
res=l
ansf=(a[0] if a else 0)
while st<=ed:
    m=(st+ed)//2
    t,f=F(m)
    if t:
        res,ansf=m,f
        ed=m-1
    else:
        st=m+1
print(res,ansf)