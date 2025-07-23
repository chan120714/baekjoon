from collections import defaultdict

a=defaultdict(set)

n=int(input())
k=[list(map(int,input().split())) for i in range(n)]


for i in k:
    a[i[0]].add(i[1])

k.sort()


res=0
for i in range(n):
    for j in range(i+1,n):
        if k[i][0]==k[j][0] or k[i][1]==k[j][1]:
            continue

        if (k[j][1] in a[k[i][0]]) and (k[i][1] in a[k[j][0]]):
            res+=1
print(res//2)
