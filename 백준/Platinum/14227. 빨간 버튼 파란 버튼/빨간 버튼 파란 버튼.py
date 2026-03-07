a,b,c,d=map(int,input().split());x=b-a;y=d-c;r=1e9
for k in range(32):
 if x<<k==y and(m:=c-(a<<k))>=0 and d-(b<<k)==m:r=min(r,k+m//(1<<k)+(m%(1<<k)).bit_count())
print(r if r<1e9 else-1)