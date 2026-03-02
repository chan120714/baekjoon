n,m=map(int,input().split())
r={}
c={}
for _ in' '*(n+m):
 x,y=map(int,input().split())
 r[x]=r.get(x,0)^1
 c[y]=c.get(y,0)^1
print("YES"if not any(r.values())and not any(c.values())else"NO")