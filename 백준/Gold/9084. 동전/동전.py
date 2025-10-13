for _ in' '*int(input()):
 input()
 d=[0]*10322;d[0]=1
 a=list(map(int,input().split()))
 b=int(input())
 for i in a:
  for j in range(i,b+1):d[j]+=d[j-i]
 print(d[b])
