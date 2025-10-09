h=['H','A','P','Y']
s=['S','A','D']
ha=0
sa=0

for i in input():
    if i in h:
        ha+=1
    if i in s:
        sa+=1

if ha==sa:
    print('50.00')
else:
    k=ha*100000//(sa+ha)
    t=k%1000
    t=t//10+(k%10>=5)
    print('%d.%.2d'%(k//1000,t))
