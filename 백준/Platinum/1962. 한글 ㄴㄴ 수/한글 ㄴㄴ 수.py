a={1 : {'ㅇ','ㅣ','ㄹ'},2:{'ㅇ','ㅣ'},3:{'ㅅ','ㅏ','ㅁ'},
       4:{'ㅅ','ㅏ'},5:{'ㅇ','ㅗ'},6:{'ㅇ','ㅠ','ㄱ'},
       7:{'ㅊ','ㅣ','ㄹ'},8:{'ㅍ','ㅏ','ㄹ'},9:{'ㄱ','ㅜ'}
}
b={10:{'ㅅ','ㅣ','ㅂ'},100:{'ㅂ','ㅐ','ㄱ'},1000:{'ㅊ','ㅓ','ㄴ'}}
c={10**4:{'ㅁ','ㅏ','ㄴ'},10**8:{'ㅇ','ㅓ','ㄱ'},
   10**12:{'ㅈ','ㅗ'},10**16:{'ㄱ','ㅕ','ㅇ'},10**20:{'ㅎ','ㅐ'},
   10**24:{'ㅈ','ㅏ'},10**28:{'ㅇ','ㅑ'},10**32:{'ㄱ','ㅜ'},
   10**36:{'ㄱ','ㅏ','ㄴ'},10**40:{'ㅈ','ㅓ','ㅇ'},10**44:{'ㅈ','ㅐ'},
   10**48:{'ㄱ','ㅡ'}
}

ten=list(c.keys())
ten.sort()
for __ in range(int(input())):
    n,m=map(int,input().split())
    t=list(map(str,input().split()))

    기수_1=set(range(1,10))
    cur=set()
    
    for j in t:
        for i in range(1,10):
            if j in a[i]:
                cur.add(i)
    기수_1-=cur
    
    기수_2=set()
    for i in b:
        기수_2.add(i)
    cur=set()
    for j in t:
        for i in [10,100,1000]:
            if j in b[i]:
                cur.add(i)
    기수_2-=cur

    기수_3=set()
    for i in c:
        기수_3.add(i)
    cur=set()
    for j in t:
        for i in c:
            if j in c[i]:
                cur.add(i)
    기수_3-=cur

    기수_4=[]
    for i in range(1,10000):
        a0,a1,a2,a3=i%10,(i//10)%10,(i//100)%10,(i//1000)
        ist=1
        if a3:
            ist=(1000 in 기수_2) and (a3 in 기수_1)
        if ist and a2:
            ist=(100 in 기수_2) and (a2 in 기수_1)
        if ist and a1:
            ist=(10 in 기수_2) and (a1 in 기수_1)
        if ist and a0:
            ist=(a0 in 기수_1)
        if ist:
            기수_4.append(i)


    pre=[0]*13
    for i in range(1,13):
        pre[i]=pre[i-1]+(ten[i-1] in 기수_3)

    res=0
    for i in range(12,0,-1):
        if pre[i]==pre[i-1]:continue
        
        if (1+len(기수_4))**(1+pre[i])>n and (1+len(기수_4))**(pre[i])<=n:
            v=n//((1+len(기수_4))**(pre[i]))
            n-=v*((1+len(기수_4))**(pre[i]))
            res+=ten[i-1]*기수_4[v-1]
    if n>len(기수_4):
        res=-1
    elif n:
        res+=기수_4[n-1]
    print(res)
