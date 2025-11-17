a,b=map(int,input().split())
c=[]
d=[]
e=[]
d.append('WBWBWBWB')
d.append('BWBWBWBW')
d.append('WBWBWBWB')
d.append('BWBWBWBW')
d.append('WBWBWBWB')
d.append('BWBWBWBW')
d.append('WBWBWBWB')
d.append('BWBWBWBW')
e.append('BWBWBWBW')
e.append('WBWBWBWB')
e.append('BWBWBWBW')
e.append('WBWBWBWB')
e.append('BWBWBWBW')
e.append('WBWBWBWB')
e.append('BWBWBWBW')
e.append('WBWBWBWB')
g=64
for i in range(a):
    c.append(str(input()))
for i in range(a-7):
    for j in range(b-7):
        z=0
        f=0
        for k in range(8):
            for l in range(8):
                if c[k+i][l+j]!=d[k][l]:
                    z+=1
                if c[k+i][l+j]!=e[k][l]:
                    f+=1
        g=min(z,f,g)
print(g)