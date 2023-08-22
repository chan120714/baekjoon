a=int(input())
gr=[list(map(int,input().split())) for i in range(a)]
s=0
for i in range(a):
   if i==a-1:
       s+=gr[i][0]*gr[0][1]
       s-=gr[0][0]*gr[i][1]
       continue
   s+=gr[i][0]*gr[i+1][1]
   s-=gr[i+1][0]*gr[i][1]
s=abs(s)
print("%.1f"%(s/2))