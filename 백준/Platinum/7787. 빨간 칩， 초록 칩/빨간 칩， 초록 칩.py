r,g=map(int,input().split())
print('B'*(r&-r==g&-g)or'A','player wins')