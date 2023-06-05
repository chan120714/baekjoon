a,b,c=map(int,input().split())
def d(a,b,c):
    if b==1:
        return a%c
    if b%2==0:
        return(d(a,b//2,c)**2)%c
    else:
        return((d(a,b//2,c)**2)*a)%c
print(d(a,b,c))