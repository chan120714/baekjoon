import sys
input=sys.stdin.readline
from collections import*
n=int(input())
q=deque()
a=list(map(int,input().split()))
for i in a:
    q.append(i)
que=[]
a=1
while a!=n:
    if len(q)==0:
        if que[-1]!=a:
            print("Sad")
            exit()
        else:
            a+=1
            que.pop()
    elif len(que)==0:
        if q[0]!=a:
            que.append(q.popleft())
        else:
            a+=1
            q.popleft()
    else:
        if q[0]==a:
            a+=1
            q.popleft()
        elif que[-1]==a:
            a+=1
            que.pop()
        else:
            que.append(q.popleft())
    if len(q)+len(que)==0:
        break
print("Nice")