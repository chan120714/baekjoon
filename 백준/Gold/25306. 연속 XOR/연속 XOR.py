a,b=map(int,input().split())
if a%2==0:
    print([b,1,b^1,0][(b-a)%4])
else:
    print([a,a^b,a-1,(a-1)^b][(b-a)%4])