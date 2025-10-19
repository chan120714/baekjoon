import sys
input=sys.stdin.readline
for _ in range(int(input())):
    n=int(input())
    a=input().rstrip()
    ist=0
    for i in range(1,n*2,2):
        if ist:
            if a[i+1]!='0':
                ist+=1
        elif a[i]=='-':
            ist+=1
    print('NO'if ist>1 else'YES')