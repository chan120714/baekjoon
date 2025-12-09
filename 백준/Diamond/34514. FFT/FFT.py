a=[0,3]
b=[0,[0,1,1]]
for i in range(2,1000001):a+=i+1+1,;b+=[0,1,i],
for i in range(2,1000001):
 for j in range(i*i,1000001,i):
  if a[j]<i+j//i+1:continue
  a[j]=i+j//i+1
  b[j]=[0,i,j//i]
for i in range(2,1000001):
 for j in range(1,min(i,99)):
  if a[j]+a[i-j]-2<a[i]:
   a[i]=a[j]+a[i-j]-2
   b[i]=[1,i-j,j]
for n in[*open(0)][1:]:
 n=int(n)
 s='FF'
 e=[[1,2]]
 f=2
 p=3
 q=[]
 def d(k):
  if b[k][0]:d(b[k][1]);d(b[k][2]);return
  q.append([b[k][1],b[k][2]])
 d(n)
 q.sort(reverse=1)
 if len(q)>1 and q[-1]==q[-2]==[1,1]:q=q[:-2]+[[2,1]]
 q.sort(reverse=1)
 for x,y in q:
  t=p
  s+='F'*(x-1)+'T'*y
  for i in range(x-1):e.append([f,p+i])
  p+=x-1
  for i in range(y):e.append([f,p+i])
  p+=y
  f=t
 print(p-1)
 print(s)
 for i in e:print(*i)