n,k=map(int,input().split())
print(n,'=',end=' ')

ist=0
if k==1:
    p=[0]*10
    for i in range(len(str(n))):
        for j in range(int(str(n)[-i-1])):
            p[i]+=1

    
    for i in range(10):
        cur=0
        for j in range(10):
            if p[j]:
                cur+=10**j
                p[j]-=1
        if cur:
            if ist:print('+ ',end='')
            print(cur,end=' ')
            ist=1
if k==2:
    p=[0]*10
    t=n%k*5
    n//=k
    for i in range(len(str(n))):
        for j in range(int(str(n)[-i-1])):
            p[i]+=1

    
    for i in range(10):
        cur=0
        for j in range(10):
            if p[j]:
                cur+=2*10**j
                p[j]-=1
        if cur:
            if ist:print('+ ',end='')
            print(cur,end='')
            if t:print('.2',end=' ');t-=1
            else:print('',end=' ')
            ist=1
        elif t:
            if ist:print('+ ',end='')
            print('0.2',end=' ')
            ist=1
            t-=1
if k==3:
    p=[0]*10
    t=n%k*3
    n//=k
    for i in range(len(str(n))):
        for j in range(int(str(n)[-i-1])):
            p[i]+=1

    
    for i in range(10):
        cur=0
        for j in range(10):
            if p[j]:
                cur+=3*10**j
                p[j]-=1
        if cur:
            if ist:print('+ ',end='')
            print(cur,end='')
            if t:print('.(3)',end=' ');t-=1
            else:print('',end=' ')
            ist=1
        elif t:
            if ist:print('+ ',end='')
            print('0.(3)',end=' ')
            ist=1
            t-=1
if k==4:
    p=[0]*10
    t=n%k*5
    o=0
    if t>=10:
       o+=5
       t-=10
    n//=k
    for i in range(len(str(n))):
        for j in range(int(str(n)[-i-1])):
            p[i]+=1

    
    for i in range(10):
        cur=0
        for j in range(10):
            if p[j]:
                cur+=4*10**j
                p[j]-=1
        if cur:
            if ist:print('+ ',end='')
            print(cur,end='')
            if o:
                print('.4',end=' ');o-=1
            elif t:
                if t%5<2:print('.44',end=' ');t-=1
                else:print('.04',end=' ');t-=1
            else:print('',end=' ')
            ist=1
        elif t+o:
            if ist:print('+ ',end='')
            if o:print('0.4',end=' ');o-=1
            elif t%5<2:print('0.44',end=' ');t-=1
            else:print('0.04',end=' ');t-=1
            ist=1
if k==5:
    p=[0]*10
    t=n%k*2
    n//=k
    for i in range(len(str(n))):
        for j in range(int(str(n)[-i-1])):
            p[i]+=1

    
    for i in range(10):
        cur=0
        for j in range(10):
            if p[j]:
                cur+=5*10**j
                p[j]-=1
        if cur:
            if ist:print('+ ',end='')
            print(cur,end='')
            if t:print('.5',end=' ');t-=1
            else:print('',end=' ')
            ist=1
        elif t:
            if ist:print('+ ',end='')
            print('0.5',end=' ')
            ist=1
            t-=1
if k==6:
    p=[0]*10
    t=n%k
    o=[0,6,3,5,6,8][t]
    db=[[],
        ['(6)','0(6)','0(6)','0(6)','0(6)','0(6)'],
        ['(6)','(6)','(6)'],
        ['6','6','6','6','6'],
        ['(6)','(6)','(6)','(6)','(6)','(6)'],
        ['6','6','6','6','6','(6)','(6)','(6)']]
    n//=k
    for i in range(len(str(n))):
        for j in range(int(str(n)[-i-1])):
            p[i]+=1

    
    for i in range(100):
        cur=0
        for j in range(10):
            if p[j]:
                cur+=6*10**j
                p[j]-=1
        if cur:
            if ist:print('+ ',end='')
            print(cur,end='')
            if o:
                print('.'+db[t][o-1],end=' ');o-=1
            else:print('',end=' ')
            ist=1
        elif o:
            if ist:print('+ ',end='')
            if o:print('0.'+db[t][o-1],end=' ');o-=1
            ist=1
if k==7:
    db=[['000700','000707','000707','000777','070777','070777','077777','7'],
        ['070000','070700','070700','077700','077707','077707','777707','7'],
        ['007000','007070','007070','007770','707770','707770','777770','7'],
        ['000007','070007','070007','770007','770707','770707','770777','7'],
        ['000070','700070','700070','700077','707077','707077','707777','7'],
        ['700000','707000','707000','777000','777070','777070','777077','7'],
        ]
    p=[0]*10
    t=n%k
    o=0
    if t:o=8
    t-=1
    n//=k
    for i in range(len(str(n))):
        for j in range(int(str(n)[-i-1])):
            p[i]+=1

    for i in range(100):
        cur=0
        for j in range(10):
            if p[j]:
                cur+=7*10**j
                p[j]-=1
        if cur:
            if ist:print('+ ',end='')
            print(cur,end='')
            if o:print('.('+db[t][o-1]+')',end=' ');o-=1
            else:print('',end=' ')
            ist=1
        elif o:
            if ist:print('+ ',end='')
            print('0.('+db[t][o-1]+')',end=' ')
            o-=1
            ist=1
if k==8:
    db=[[],
        ['888','008','008','008','088'],
        ['88','08','08','08','88'],
        ['08','08','088','088','888','888','888'],
        ['8','8','8','8','8'],
        ['8','808','808','808','888','888'],
        ['8','8','88','88','88','88','88'],
        ['8','88','88','888','888','888','888','888']]
    p=[0]*10
    t=n%k
    o=len(db[t])
    n//=k
    for i in range(len(str(n))):
        for j in range(int(str(n)[-i-1])):
            p[i]+=1

    
    for i in range(100):
        cur=0
        for j in range(10):
            if p[j]:
                cur+=8*10**j
                p[j]-=1
        if cur:
            if ist:print('+ ',end='')
            print(cur,end='')
            if o:print('.'+db[t][o-1],end=' ');o-=1
            else:print('',end=' ')
            ist=1
        elif o:
            if ist:print('+ ',end='')
            if o:print('0.'+db[t][o-1],end=' ');o-=1
            ist=1
if k==9:
    p=[0]*10
    t=n%k
    n//=k
    for i in range(len(str(n))):
        for j in range(int(str(n)[-i-1])):
            p[i]+=1

    
    for i in range(10):
        cur=0
        for j in range(10):
            if p[j]:
                cur+=9*10**j
                p[j]-=1
        if cur:
            if ist:print('+ ',end='')
            print(cur,end='')
            if t:print('.(9)',end=' ');t-=1
            else:print('',end=' ')
            ist=1
        elif t:
            if ist:print('+ ',end='')
            print('0.(9)',end=' ')
            ist=1
            t-=1
    
