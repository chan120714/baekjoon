M=10**9+7
a=[7]
b=[3]
for i in range(6**8):
 a+=[(a[i]*3+b[i]*4)%M]
 b+=[(a[i]+2*b[i])%M]
for l in[*open(0)][1:]:print(a[int(l)-1])