import math
a=int(input())
n=list(map(int,input().split()))
s=[0]
k=0
for i in range(a*2):
 s.append(n[i%a]+s[-1])
for i in range(a):
 for j in range(i+1,i+a+1):
  if s[j]-s[i]<0:
   k+=math.ceil((s[i]-s[j])/s[a])
print(k)