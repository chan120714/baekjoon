s=0
for i in range(1,int(input())+1):
    a=[]
    for j in range(len(str(i))):
        a.append(int(str(i)[j]))
    if i%sum(a)==0:
        s+=1
print(s)