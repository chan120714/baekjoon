import sys
input=sys.stdin.readline
for i in range(int(input())):
    n,m=map(int,input().split())
    k=m-n
    p=int((k)**(1/2))-2
    for i in range(p,k):
        p=i*(i+1)//2
        if p*2>=k:
            print(i*2)
            break
        elif p*2+(i+1)>=k:
            print(i*2+1)
            break