a=[0,0,1,0,1,1]

for i in range(1000):
    if a[-3]==0 or a[-4]==0 or a[-1]==0:
        a.append(1)
    else:
        a.append(0)
print('SK'*a[int(input())]or'CY')