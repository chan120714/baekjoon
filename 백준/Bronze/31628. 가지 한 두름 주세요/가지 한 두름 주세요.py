a=[input().split()for i in' '*10]
for i in range(100):
 x,y=i//10,i%10
 k={0};t={0}
 for j in range(10):k.add(a[x][j]);t.add(a[j][y])
 if len(k)<3 or len(t)<3:print(1);exit()
print(0)