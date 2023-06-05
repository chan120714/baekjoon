import sys
input=sys.stdin.readline
a=input().rstrip()

def qwe():
    t=len(a)
    start,end=0,t-1
    while start<end:
        if a[start]!=a[end]:
            return t
        start+=1
        end-=1
    start,end=0,len(a)-2
    while start<end:
        if a[start]!=a[end]:
            return t-1
        start+=1
        end-=1
    return -1
print(qwe())