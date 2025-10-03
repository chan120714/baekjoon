n=int(input())
m,k=map(int,input().split())
*a,=map(int,input().split())
a.sort(reverse=True)
res=0
cur=0
for i in a:
    cur+=i
    res+=1
    if cur>=m*k:
        break
if cur<m*k:print("STRESS")
else:print(res)
