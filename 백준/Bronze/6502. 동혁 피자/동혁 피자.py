t=1
while 1:
    a=list(map(int,input().split()))
    if len(a)==1:
        break
    if 4*a[0]**2>=a[1]**2+a[2]**2:
        print(f'Pizza {t} fits on the table.')
    else:
        print(f'Pizza {t} does not fit on the table.')
    t+=1