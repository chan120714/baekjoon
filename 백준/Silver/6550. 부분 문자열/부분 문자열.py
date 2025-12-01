while 1:
    try:
        a,b=input().split()
        cnt=0
        for i in b:
            
            if a[cnt]==i:cnt+=1
            if cnt==len(a):break
        if cnt==len(a):print("Yes")
        else:print('No')
    except EOFError:
        break