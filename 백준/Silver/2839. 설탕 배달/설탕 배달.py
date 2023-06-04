a=int(input())
b=0
while a>0:
	if a%5==0:
		b+=a//5
		a=0
	elif a>2:
		a-=3
		b+=1
	else:
		a=0
		b=-1
print(b)