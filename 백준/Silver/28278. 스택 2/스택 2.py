import sys
input=sys.stdin.readline
def push(n):
    b.append(n)
def pop():
    if len(b)==0:
        print(-1)
    else:
        print(b.pop(-1))
def size():
    print(len(b))
def empty():
    if len(b)==0:
        print(1)
    else:
        print(0)
def top():
    if len(b)==0:
        print(-1)
    else:
        print(b[-1])
a=int(input())
b=[]
for i in range(a):
    c=list(map(str,input().split()))
    if c[0]=='1':
        push(c[1])
    elif c[0]=='2':
        pop()
    elif c[0]=='3':
        size()
    elif c[0]=='4':
        empty()
    elif c[0]=='5':
        top()