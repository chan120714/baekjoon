import sys
input=sys.stdin.readline
sys.setrecursionlimit(10000)
c=10**9+7
def pow(n):
    if n<1:
        return 1
    if n==1:
        return 2
    if n%2:
        return (pow(n//2)**2*2)%c
    else:
        return (pow(n//2)**2)%c
for i in range(int(input())):
    print(pow(int(input())-2)%c)