import sys
input=sys.stdin.readline

n=int(input())
a=sorted(list(map(int,input().split())))
a.reverse()
k=0
for i in a:
    if k>=3:
        print(i*i)
        exit()
    k+=1
print(0)