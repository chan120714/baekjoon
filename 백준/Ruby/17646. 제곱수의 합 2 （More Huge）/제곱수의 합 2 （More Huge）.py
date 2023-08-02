import sys
input=sys.stdin.readline
from math import*
from random import*
from decimal import*
from collections import Counter
p=[2,3,5,7,11,13,17,19,23,29,31,37,41]

def number(n,m):
    if int(sqrt(n))**2==n:
        return 1
    if n%8==7:
        return 4
    a=[]
    while m>1:
        k=rho(m)
        a.append(k)
        m//=k
    a.sort()
    cnt=list(Counter(a).items())
    for q,w in cnt:
        if q%4==3 and w%2==1:
            return 3
    return 2
def pow(x,y,p):
    if y<2:
        return (x**y)%p
    if y%2:
        return (pow(x,y//2,p)**2*x)%p
    else:
        return (pow(x,y//2,p)**2)%p

def mil(n,a):
    s,d=0,n-1
    while not d%2:
        s+=1
        d//=2
    x=pow(a,d,n)
    if x==1 or x+1==n:
        return True
    for i in range(s-1):
        x=pow(x,2,n)
        if x+1==n:
            return True
    return False

def pri(n):
    if n in p:
        return True
    if n==1 or not n%2:
        return False
    for k in p:
        if not mil(n,k):
            return False
    return True

def rh(n,c,d):
    return (n**2+c)%d

def rho(n):
    if pri(n):
        return n
    if n==1:
        return 1
    if not n%2:
        return 2
    x,c,d=randint(2,n-1),randint(1,n-1),1
    y=x
    while d==1:
        x=rh(x,c,n)
        y=rh(y,c,n)
        y=rh(y,c,n)
        d=gcd(n,abs(x-y))
        if d==n:
            return rho(n)
    if pri(d):
        return d
    return rho(d)

def legendre(a,p):
    return pow(a,(p-1)//2,p)

def tone(n,p):
    q=p-1
    s=0
    while q%2==0:
        q//=2
        s+=1
    if s==1:
        return pow(n,(p+1)//4,p)
    for x in range(2,p):
        if p-1==legendre(x,p):
            break
    c=pow(x,q,p)
    r=pow(n,(q+1)//2,p)
    t=pow(n,q,p)
    m=s
    u=0
    while (t-1)%p!=0:
        u=(t*t)%p
        for i in range(1,m):
            if (u-1)%p==0:
                break
            u=(u*u)%p
        b=pow(c,1<<(m-i-1),p)
        r=(r*b)%p
        c=(b*b)%p
        t=(t*c)%p
        m=i
    return r

def corn(m):
    r_0=tone(m-1,m)
    r_1=m%r_0
    while r_1**2>m:
        r_0,r_1=r_1,r_0%r_1
    s=(m-r_1**2)//1
    if isqrt(s)**2==s:
        return r_1,isqrt(s)
    else:
        r_0=m-tone(m-1,m)
        r_1=m%r_0
        while r_1**2>m:
            r_0,r_1=r_1,r_0%r_1
        s=(m-r_1**2)//1
        if isqrt(s)**2==s:
            return r_1,isqrt(s)

def two(n):
    a=[]
    q=[]
    while n>1:
        x=rho(n)
        n//=x
        a.append(x)
    res=list(set(a))
    squ=[0 for i in range(len(res))]
    for i in a:
        squ[res.index(i)]+=1
    z,x,c=1,1,0
    for i in range(len(res)):
        z*=res[i]**(squ[i]//2)
        if squ[i]%2:
            if res[i]==2:
                x,c=abs(x-c),x+c
            else:
                t=corn(res[i])
                x,c=abs(x*t[0]-c*t[1]),c*t[0]+x*t[1]
    return z*x,z*c 

def three(s,n):
    a=1
    while number(n,n-a**2)!=2:
        a+=1
    k=two(n-a**2)
    return k[0]*(2**s),k[1]*(2**s),a*(2**s)


n=int(input())
m=n
s=0
while not n%4:
    n//=4
    s+=1
numb=number(n,m)
if numb==1:
    print(1,'\n%d'%isqrt(m))
if numb==2:
    print(2)
    print(*sorted(two(m)))
if numb==3:
    print(3)
    print(*sorted(three(s,n)))
if numb==4:
    print(4)
    t=sorted(three(0,n-1))
    print(2**s,end=' ')
    for i in t:
        print(i*(2**s),end=' ')