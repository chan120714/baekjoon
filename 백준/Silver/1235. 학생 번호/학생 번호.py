n=int(input())
a=[input() for i in range(n)]
l=len(a[0])

for k in range(1,l+1):
    s=set()
    ist=1
    for i in a:
        if i[-k:] in s:
            ist=0
            break
        s.add(i[-k:])
    if ist:
        print(k)
        break