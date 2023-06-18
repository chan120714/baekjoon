import sys
input=sys.stdin.readline
from collections import deque
for i in range(int(input())):
    a=input().rstrip()
    n=int(input())
    graph=list(map(str,input().split(",")))
    graph[0]=graph[0][1:]
    graph[-1]=graph[-1][0:-2]
    q=deque()
    reverse=0
    error=False
    for i in range(n):
        q.append(int(graph[i]))
    for i in range(len(a)):
        if a[i]=="R":
            reverse^=1
        else:
            if len(q)==0:
                print("error")
                error=True
                break
            if reverse==0:
                q.popleft()
            else:
                q.pop()
    k=len(q)
    if reverse==1 and k!=0:
        q.reverse()
    if error==True:
        continue
    print('[',end='')
    for i in range(k):
        print(q[i],end='')
        if i!=k-1:
            print(',',end='')
    print(']')