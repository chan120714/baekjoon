graph=[[0 for i in range(100)] for i in range(100)]
for i in range(int(input())):
    a,b=map(int,input().split())
    for i in range(10):
        for j in range(10):
            graph[i+a][j+b]=1
summ=0
for i in range(100):
    summ+=sum(graph[i][0:])
print(summ)