r,g=map(int,input().split())
k=0
while r%2<1:
    r//=2;k+=1
while g%2<1:
    g//=2;k-=1
print('A'*(k!=0)or'B','player wins')