s={a:=0}
for i in range(1+int(input())):s.add(a:=a+i*2*(a<i or a-i in s)-i)
print(a)