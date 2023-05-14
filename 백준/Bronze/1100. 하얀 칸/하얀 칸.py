graph=[list(map(str,input())) for i in range(8)]
a=0
for i in range(8):
    for j in range(8):
        if i%2==0:
            if j%2==0:
                if graph[i][j]=='F':
                    a+=1
        else:
            if j%2==1:
                if graph[i][j]=='F':
                    a+=1
print(a)