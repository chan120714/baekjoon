from math import*
n=int(input())
a=list(map(int,input().split()))
a.sort()
res=0
for i in range(n-1):
    if gcd(a[i],a[i+1])==1:
        continue
    else:
        for j in range(a[i]+1,a[i+1]):
            if gcd(a[i],j)==gcd(a[i+1],j)==1:
                res+=1
                break
        else:
            res+=2
print(res)