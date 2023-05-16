a=int(input())
b=1000000
c=1500000
def f(k):
    n,m=0,1
    for i in range(k):
        n,m=m%b,(n+m)%b
    return n
print(f(a%c))