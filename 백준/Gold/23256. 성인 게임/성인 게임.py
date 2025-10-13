M=10**9+7
a=[7]
b=3
for i in range(6**8):a+=(a[i]*3+b*4)%M,;b=(a[i]+2*b)%M
_,*s=map(int,open(0))
for l in s:print(a[l-1])