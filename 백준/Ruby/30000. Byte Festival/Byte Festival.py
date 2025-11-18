from math import gcd
g=[[1]*1112 for i in range(1112)]
for i in range(1111):g[i][1]=0;g[1][i]=0;g[i][1111]=0;g[1111][i]=0
for i in range(1111):
    for j in range(1111):
        if gcd(i,j)==1:g[i][j]=0
for i in range(1111):
    for k in range(3):
        s=''
        for j in range(1111):
            if g[i][j]<1:print(' '*3,end='')
            else:
                if k<1:print('#'+' #'[g[i-1][j]<1]+'#',end='')
                elif k<2:print(' #'[g[i][j-1]<1]+' '+' #'[g[i][j+1]<1],end='')
                else:print('#'+' #'[g[i+1][j]<1]+'#',end='')
        print()
