n=list(map(str,input()))
a=''
p=[]
for i in n:
	if '0'<=i<='9':
		a+=i
	else:
		p.append(int(a))
		p.append(i)
		a=''
p.append(int(a))
res=p[0]
nega=0
temp=0
for i in range(1,len(p)):
	if p[i]=='-':
		if nega==1:
			res-=temp
			temp=0
			continue
		else:
			res+=temp
			temp=0
			nega=1
			continue
	if p[i]=='+':
		continue
	temp+=p[i]
if nega==1:
	res-=temp
else:
	res+=temp
print(res)