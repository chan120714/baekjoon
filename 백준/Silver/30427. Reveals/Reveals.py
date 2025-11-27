input()
n=int(input())
a=[input().rstrip() for i in range(n)]
m=int(input())
b=set([input().rstrip() for i in range(m)])

a=set(a)
if 'dongho' in a:
    print('dongho')
    exit()

if len(set(a)-set(b))==1:
    print(*list(set(a)-set(b)))
    exit()

if (not 'bumin' in b) and ('bumin' in a):
    print('bumin')
    exit()

if (not 'cake' in b) and ('cake' in a):
    print('cake')
    exit()

if (not 'lawyer' in b) and ('lawyer' in a):
    print('lawyer')
    exit()

a=sorted(list(a))

for i in a:
    if i=='swi':continue
    if not i in b:
        print(i)
        exit()
print('swi')