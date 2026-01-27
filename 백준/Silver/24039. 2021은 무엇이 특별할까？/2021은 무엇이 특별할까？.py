p=[]
for i in range(2,900):
    for j in range(2,i):
        if i%j==0:
            break
    else:
        p.append(i)
n=int(input())

for i in range(1,len(p)):
    if p[i]*p[i-1]>n:
        print(p[i]*p[i-1])
        break