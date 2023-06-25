from collections import deque
import sys
input=sys.stdin.readline
def push_back(n):
    b.append(n)
def push_front(n):
    b.appendleft(n)
def pop_front():
    if len(b)==0:
        print(-1)
    else:
        print(b.popleft())
def pop_back():
    if len(b)==0:
        print(-1)
    else:
        print(b.pop())
def size():
    print(len(b))
def empty():
    if len(b)==0:
        print(1)
    else:
        print(0)
def front():
    if len(b)==0:
        print(-1)
    else:
        print(b[0])
def back():
    if len(b)==0:
        print(-1)
    else:
        print(b[-1])
a=int(input())
b=deque()
for i in range(a):
    c=list(map(str,input().split()))
    if c[0]=='push_front':
        push_front(c[1])
    elif c[0]=='push_back':
        push_back(c[1])
    elif c[0]=='pop_front':
        pop_front()
    elif c[0]=='pop_back':
        pop_back()
    elif c[0]=='size':
        size()
    elif c[0]=='empty':
        empty()
    elif c[0]=='front':
        front()
    elif c[0]=='back':
        back()