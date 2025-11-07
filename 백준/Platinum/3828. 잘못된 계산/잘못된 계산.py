while 1:
    n=int(input())
    if n==0:break
    tn=[]

    for i in range(n+3):
        d=[]
        for j in range(n,-1,-1):
            d.append(i**j)
        d.append(0)
        d.append(float(input()))
        tn.append(d)
        
    n+=2
    for x in range(n+1):
        a=[]
        for i in range(n+1):
            if i==x:continue
            a.append([*tn[i]])


        for i in range(n):
            pivot=i

            for j in range(i+1,n):
                if abs(a[j][i])>abs(a[pivot][i]):
                    pivot=j
            if a[pivot][i]==0:
                continue

            a[pivot],a[i]=a[i],a[pivot]
            
            for j in range(i+1,n):
                t=a[j][i]/a[i][i]
                for k in range(i,n+1):
                    a[j][k]-=a[i][k]*t


        if abs(a[-1][-1])<1e-4:
            break
    print(x)
