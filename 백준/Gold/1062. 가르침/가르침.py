import sys
input=sys.stdin.readline

n,k=map(int,input().split())
a=[input().rstrip() for i in range(n)]

t=[0]*26
t[0]=1
t[2]=1
t[8]=1
t[13]=1
t[19]=1

res=0
for i in range(1<<21):
    p=5
    t=[0]*26
    for j in range(26):
        if j in [0,2,8,13,19]:
            t[j]=1
            continue
        if i&1:
            t[j]=1
            p+=1
        i>>=1
    ret=0
    if p!=k:
        continue
    
    for j in a:
        cur=1
        for p in j:
            if t[ord(p)-97]==0:
                cur=0
                break
        ret+=cur
    res=max(res,ret)
print(res)
