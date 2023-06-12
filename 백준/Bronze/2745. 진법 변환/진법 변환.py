a,b=map(str,input().split())
b=int(b)
c=len(a)
d=0
for i in range(c):
    e=ord(a[i])
    if e>=65:
        e-=55
    else:
        e=int(a[i])
    d+=e*(b**(c-1-i))
print(d)