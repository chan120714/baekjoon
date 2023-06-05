import sys
input=sys.stdin.readline
for _ in range(int(input())):
    n,m,k=map(int,input().split())
    arr=[0]*(n+1)
    tree=[0]*(n+1)
    def sm(i):
        res=0
        while i>0:
            res+=tree[i]
            i-=(i&-i)
        return res
    def update(i,d):
        while i<=n:
            tree[i]+=d
            i+=(i&-i)
    def s_s(n,m):
        return sm(m)-sm(n-1)
    for i in range(m+k):
        a,b,c=map(str,input().split())
        b,c=int(b),int(c)
        if a=="P":
            update(b,c)
            arr[b]+=c
        else:
            print(s_s(b,c))