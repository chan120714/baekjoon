s,a,b,c=map(int,input().split())
M=10**9+7
f=[1]
for i in range(8**7):f+=f[i]*-~i%M,
f+=[r:=0]*8**7
for t in range(s+1):
    try:r=(r+(-1)**t*f[s]*pow(f[s-t],2,M)*pow(f[a]*f[b]*f[c]*f[t]*f[s-t-a]*f[s-t-b]*f[s-t-c],-1,M))%M
    except:pass
print(r)