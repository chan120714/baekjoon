def ccw(p1,p2,p3):
    p=(p2[0]-p1[0])*(p3[1]-p1[1])-(p3[0]-p1[0])*(p2[1]-p1[1])
    if p>0:
        return 1#시계
    elif p==0:
        return 0#직선
    return -1#반시계
pos=[list(map(int,input().split())) for i in range(3)]
print(ccw(pos[0],pos[1],pos[2]))