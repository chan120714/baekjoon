x=int(input())
if x==0:print('BOJ 30000')
elif x==1:
    n=989345275647
    while n>1:
        print(n)
        if n%2:
            n*=3
            n+=1
        else:
            n//=2
    print(1)
elif x==2:
    t=['one','ten','one hundred']
    s='illion'
    print(*t,sep='\n')
    for i in t:print(i,'thousand')
    for a in['','millia','duomillia','tremillia','quattuormillia','quinmillia','sexmillia','septenmillia','octomillia','novemmillia']:
        for x in['','cen','duocen','trecen','quadringen','quingen','sescen','septingen','octingen','nongen']:
            if x=='' and a!='':
                for j in t:print(j,a+x+'t'+s)
            elif x!='':
                for j in t:print(j,a+x+s)        
            for i in['m','b','tr','quadr','quint','sext','sept','oct','non']:
                for j in t:print(j,a+x+i+s)
            for i in['dec','vigint','trigint','quadragint','quinquagint','sexagint','septuagint','octogint','nonagint']:
                for j in['','un','do','tre','quattuor','quin','sex','septen','octo','novem']:
                    for k in t:print(k,a+x+j+i+s)
