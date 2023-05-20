a=[0]*11
for i in range(2047):
    b=list(map(int,input().split()))
    for i in range(11):
        a[i]^=b[i]
print(*a)