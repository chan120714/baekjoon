n=int(input())
d=[0]*1002

for i in map(int,input().split()):
    d[i]+=1

for i in range(1001):
    if d[i]==0:continue
    if d[i+1]==0:
        print((str(i)+' ')*d[i],end='')
    else:
        for j in range(i+2,1001):
            if d[j]:
                print((str(i)+' ')*d[i],end='')
                print(j,end=' ')
                d[j]-=1
                break
        else:
            print((str(i+1)+' ')*d[i+1],end='')
            print((str(i)+' ')*d[i],end='')
            d[i+1]=0