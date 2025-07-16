m=int(input())
k=int(input())
a=[list(map(int,input().split())) for i in range(8)]
c=[0 for i in range(8)]
r=[0 for i in range(8)]
for i in range(8):
    for j in range(8):
        a[i][j]-=m
        c[i]+=a[i][j]
        r[j]+=a[i][j]
g=[[0 for i in range(8)]for i in range(8)]
c1=[0 for i in range(8)]
r1=[0 for i in range(8)]
for i in range(8):
    for j in range(8):
        g[i][j]=c[i]+r[j]-a[i][j]
        g[i][j]%=2
        c1[i]+=g[i][j]%2
        r1[j]+=g[i][j]%2
c2=[0 for i in range(8)]
r2=[0 for i in range(8)]
g1=[[0 for i in range(8)]for i in range(8)]
for i in range(8):
    for j in range(8):
        g1[i][j]=c1[i]+r1[j]-g[i][j]
        c2[i]+=g1[i][j]
        r2[j]+=g1[i][j]


for i in range(8):
    for j in range(8):
        if g[i][j]%2:
            if (g1[i][j]-c2[i]-r2[j]+c[i]+r[j]-a[i][j])%4==2:
                print('-',end=' ')
            else:
                print('+',end=' ')
        else:
            print('.',end=' ')
    print()