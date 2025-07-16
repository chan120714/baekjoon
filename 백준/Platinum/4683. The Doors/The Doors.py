from heapq import*
while 1:
    x=int(input())
    if x==-1:
        break
    
    a=[list(map(float,input().split())) for i in range(x)]
    t=[[]for i in range(x)]
    v=[(0,5),(10,5)]
    for i in a:
        for j in i[1:]: v.append((i[0],j))
    d=[[9999]*len(v) for i in range(len(v))]
    v.sort()
    n=len(v)
    for i in range(n):
        for j in range(i+1,n):
            ist=1
            for wx,y1,y2,y3,y4 in a:
                if (v[i][0]<wx and v[j][0]<wx) or (v[i][0]>wx and v[j][0]>wx):
                    continue
                if wx==v[i][0] and wx==v[j][0]:
                    maxv=max(v[j][1],v[i][1])
                    minv=min(v[j][1],v[i][1])
                    if not (y1<=minv<=y2 and y1<=maxv<=y2) or (y3<=minv<=y4 or y3<=maxv<=y4):
                        ist=0
                        break
                    continue
                if wx<v[i][0] or v[j][0]<wx:
                    continue
                dx=(v[j][1]-v[i][1])/(v[j][0]-v[i][0])
                h=v[i][1]+dx*(wx-v[i][0])
                if not (y1<=h<=y2 or y3<=h<=y4):
                    ist=0
                    break
            if ist:
                dist=((v[i][0]-v[j][0])**2+(v[j][1]-v[i][1])**2)**.5
                d[i][j]=dist
                d[j][i]=dist
        
    for a in range(n):
        for i in range(n):
            for j in range(n):
                d[i][j]=min(d[i][j],d[i][a]+d[a][j])
                
    print('%.2f'%d[0][-1])
