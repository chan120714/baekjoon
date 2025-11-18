P=print
x=int(input())
if x==0:P('BOJ 30000')
elif x==1:
    n=989345275647
    while n>1:
        P(n)
        if n%2:n*=3;n+=1
        else:n//=2
    P(1)
elif x==2:
    t=['one','ten','one hundred']
    s='illion'
    P(*t,sep='\n')
    for i in t:P(i,'thousand')
    k=['','','duo','tre','quattuor','quin','sex','septen','octo','novem']
    p=['dec','vig','trig','quadrag','quinquag','sexag','septuag','octog','nonag']
    for i in range(1,10):k[i]+='millia'
    for i in range(1,9):p[i]+='int'
    for a in k:
        for x in['','cen','duocen','trecen','quadringen','quingen','sescen','septingen','octingen','nongen']:
            if x=='' and a!='':
                for j in t:P(j,a+x+'t'+s)
            elif x!='':
                for j in t:P(j,a+x+s)        
            for i in['m','b','tr','quadr','quint','sext','sept','oct','non']:
                for j in t:P(j,a+x+i+s)
            for i in p:
                for j in['','un','do','tre','quattuor','quin','sex','septen','octo','novem']:
                    for k in t:P(k,a+x+j+i+s)
elif x==4:
    t=[i for i in range(126,31,-1)]
    for i in t:
        print(chr(i),end='')
elif x==6:
    print('f(x) = 8, g(x) = 2x, h(x) = ?g(x)')
    for i in range(1,30001):print(8,i*2,3*i)
    print('f(x) = f(x-1)+?, g(x) = ?g(x-1)+?g(x-2), h(x) = ?h(x-1)+?h(x-2)+?h(x-3)+?h(x-4)+?h(x-5)+?h(x-6)')
    f=9099099909999099999
    mod=1000000007
    p=[1,1]
    k=[1,10,100,1000,10000,100000]
    for i in range(30000):
        print(f,p[i],k[i])
        f+=30000
        f%=mod
        p+=(p[-1]+p[-2])%mod,
        k+=(k[-6]+k[-5]*9+k[-4]*8+k[-3]*2+k[-2]*6+k[-1])%mod,
    print('f(x) = ?x^2+?x+?, g(x) = ?^f(x), h(x) = ?x^6+?x^5+?x^4+?x^3+?x^2+?x+?')
    mod=73939133
    for i in range(1,30001):
        y=(1*(i**6))+73938466*(i**5)+185292*(i**4)+46497867*(i**3)+66865799*(i**2)+5835641*i+68502405
        y%=mod
        x=(123*(i**2)+456*i+789)
        print(x%mod,pow(30000,x,mod),y)