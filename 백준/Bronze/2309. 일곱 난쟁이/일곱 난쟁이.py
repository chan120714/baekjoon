a=[]
for i in range(9):
    a.append(int(input()))
a=sorted(a)
for i in range(9):
    for j in range(i,9):
        if sum(a)-a[i]-a[j]==100:
            for k in range(9):
                if k==i or k==j:
                    continue
                print(a[k])
            exit()