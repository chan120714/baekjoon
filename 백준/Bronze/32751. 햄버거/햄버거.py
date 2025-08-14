n=int(input())
a,b,c,d=map(int,input().split())
k=input()
if k.count('a')>a or k.count('b')>b or k.count('c')>c or k.count('d')>d:
    print('No')
elif k[0]!='a' or k[-1]!='a':
    print('No')
else:
    cur=''
    t=1
    for i in k:
        if i==cur:
            t=0
        cur=i
    print('Yes'*t or 'No')
