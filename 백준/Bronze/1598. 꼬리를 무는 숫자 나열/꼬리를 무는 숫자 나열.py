a,b=map(int,input().split())
print(abs(((b-1)//4+1)-((a-1)//4+1))+abs(((b-1)%4) - ((a-1)%4)))