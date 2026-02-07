m,t=map(int,input().split())
for _ in range(t):
 a,b,c,d=map(int,input().split());n=a*a+b*b+c*c+d*d
 try:i=pow(n,-1,m);print(a*i%m,-b*i%m,-c*i%m,-d*i%m)
 except:print(0,0,0,0)