import sys
input=sys.stdin.readline
pos=[list(map(int,input().split())) for i in range(3)]
def ccw():
    p=(pos[1][0]-pos[0][0])*(pos[2][1]-pos[0][1])-((pos[2][0]-pos[0][0])*(pos[1][1]-pos[0][1]))
    if p>0:
        return 1
    elif p==0:
        return 0
    else:
        return -1
print(ccw())