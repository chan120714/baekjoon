import sys
input=sys.stdin.readline
a=int(input())
for i in range(20000):
    print("? 1")
    sys.stdout.flush()
    a=input().rstrip()
    if a=='Y':
        print("! 1")
        sys.stdout.flush()
        break