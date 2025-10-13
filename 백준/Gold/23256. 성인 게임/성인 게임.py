M=10**9+7
a=[7,33]
b=[3,13]
for i in range(6**8):
 a+=[(a[-1]*3+b[-1]*4)%M]
 b+=[(a[-2]+2*b[-1])%M]
for l in[*open(0)][1:]:print(a[int(l)-1])