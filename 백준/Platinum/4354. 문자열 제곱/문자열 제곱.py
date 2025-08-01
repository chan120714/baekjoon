import sys
input=sys.stdin.readline
while 1:
	a=input().rstrip()
	if a=='.':
		break
	k=len(a)
	p=[]
	for i in range(1,1+len(a)):
		if k%i==0:
			p.append(i)
	for i in p:
		e,d=i,i
		tt=a[:d]
		if a.find(tt*((k-i)//i),e,k)==-1:
			continue
		else:
			print(k//i)
			break