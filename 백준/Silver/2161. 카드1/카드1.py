from collections import deque
queue= deque()
a=int(input())
for i in range(1,a+1):
    queue.append(i)
while len(queue)!=1:
    print(queue.popleft(),end=' ')
    queue.append(queue[0])
    queue.popleft()
print(queue[0])