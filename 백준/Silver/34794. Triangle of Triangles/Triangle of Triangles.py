import sys
input=sys.stdin.readline

for __ in range(int(input())):
    *a,=map(int,input().split())
    *b,=map(int,input().split())
    *c,=map(int,input().split())
    a.sort()
    b.sort()
    c.sort()
    ist=0

    for i in range(3):
        for j in range(3):
            if a[i]!=b[j]:
                continue
            for t in range(3):
                if i==t:continue
                for k in range(3):
                    re=[]
                    if k==j:continue
                    if b[k]<a[t]:
                        re.append(a[t]-b[k])
                        re.append(180-b[3-(j+k)])
                        re.append(a[3-(i+t)])
                        re.sort()
                        if re==c or re==b:
                            ist=1

    for i in range(3):
        for j in range(3):
            if a[i]!=c[j]:
                continue
            for t in range(3):
                if i==t:continue
                for k in range(3):
                    re=[]
                    if k==j:continue
                    if c[k]<a[t]:
                        re.append(a[t]-c[k])
                        re.append(180-c[3-(j+k)])
                        re.append(a[3-(i+t)])
                        re.sort()
                        if re==c or re==b:
                            ist=1
    if ist:
        print("YES")
    else:
        print("NO")