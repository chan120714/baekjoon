M=10**5
t=[0]*123123
res=[0]*123123

def u(x,v):
    while x<=10**5:
        t[x]+=v
        x+=x&-x

def q(x):
    r=0
    while x:
        r+=t[x]
        x-=x&-x
    return r

res[1]=100000
u(1,1)
for i in range(2,100001):
    v=q(i)
    res[i]=v
    u(i,1)
    u(i+v+1,-1)
print(*res[1:100001])
