from bisect import*

res=[0]
def dfs(n,i):
    res.append(n)
    for a in range(1,10):
        if not i&(1<<(a-1)):
            dfs(n*10+a,i^(1<<(a-1)))
    return

for i in range(1,10):
    dfs(i,1<<(i-1))
res.sort()
while 1:
    try:
        n=int(input())
        a=bisect_right(res,n)
        if len(res)>a:print(res[a])
        else: print(0)
    except EOFError:
        break