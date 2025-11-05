print(999,1501)
ret=0
for i in range(999):
    for j in range(i+1,999):
        if ret==1501:
            break
        print(i,j)
        ret+=1