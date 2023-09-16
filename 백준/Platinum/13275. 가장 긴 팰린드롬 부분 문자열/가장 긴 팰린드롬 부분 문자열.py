import sys
input=sys.stdin.readline
a=input().rstrip()
d=''
for i in a:
    d+=i
    d+='.'
m=[0]*200005
r,p=0,0
for i in range(len(d)):
    if i<=r:
        m[i]=min(m[2*p-i],r-i)
    else:
        m[i]=0
    while (i-m[i]>=0 and i+m[i]+1<len(d) and d[i-m[i]-1]==d[i+m[i]+1]):
        m[i]+=1
    if r<i+m[i]:
        r=i+m[i]
        p=i
print(max(m))