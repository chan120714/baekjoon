n=int(input())
r=0
for i in map(int,input().split()):r^=i-2
if input()[0]=='W':print('Whiteking'*(r>0)or'Blackking')
else:print('Whiteking'*(r<1)or'Blackking')