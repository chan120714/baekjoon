p=int(input())
k,l=map(int,input().split())
for _ in range(p):
     n=int(input())
     s=input()
     m=int(input())
     t=input()
     if k==1 or n==m:
         print('YS')
     elif n<m:
         print('Y')
     else:
         print('S')