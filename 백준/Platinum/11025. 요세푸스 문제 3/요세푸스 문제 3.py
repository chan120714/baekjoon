import sys
input=sys.stdin.readline
a,b=map(int,input().split())
j=1
for i in range(2,a+1):
    j=(j+b-1)%i+1
print(j)