while 1:
    try:
        b0,b1,b2,b3=map(float,input().split())
        t0,t1,t2,t3=map(float,input().split())

        x=[0,1]
        d0,d1,d2=(b1-t1),(b2-t2)*2,(b3-t3)*3
        if d1**2-4*d2*d0>=0:
            x0=(-d1-(d1**2-4*d2*d0)**.5)/(2*d2)
            x1=(-d1+(d1**2-4*d2*d0)**.5)/(2*d2)
            if 0<=x0<=1:
                x.append(x0)
            if 0<=x1<=1:
                x.append(x1)
        res=[]
        for i in x:
            res.append((b0-t0)+(b1-t1)*i+(b2-t2)*(i**2)+(b3-t3)*(i**3))
        print(max(res)-min(res))
    except EOFError:
        break