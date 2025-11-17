x=int(input())
if x==0:print('BOJ 30000')
elif x==1:
    n=989345275647
    while n>1:
        print(n)
        if n%2:
            n*=3
            n+=1
        else:
            n//=2
    print(1)