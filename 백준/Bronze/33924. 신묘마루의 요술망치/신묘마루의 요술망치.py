j=input
n,m=map(int,j().split())
j()
n+=n+m-3
for i in j():n=[b'24163857'[n]-49,n^4,n^3,n^7][ord(i)&3]
print(n//2+1,n%2+1)