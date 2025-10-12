P=10**9+7
N,M,K=map(int,input().split())
f=[1]
for i in range(N+M):f.append(f[-1]*-~i%P)
b=[list(map(int,input().split()))for i in' '*K]
C=lambda n,k:f[n]*pow(f[k]*f[n-k]%P,-1,P)
def s(x,y):return C(x+y,x)-sum([C(x-q+y-w,x-q)*s(q,w)for q,w in b if(x>=q and y>=w and(x,y)!=(q,w))])
print(s(N,M)%P)