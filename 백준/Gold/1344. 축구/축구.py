from math import*
n=int(input())
m=int(input())
res1=0
res2=0
for i in [2,3,5,7,11,13,17]:
    res1+=comb(18,i)*((n**i)/(100**i))*(((100-n)**(18-i))/(100**(18-i)))
    res2+=comb(18,i)*((m**i)/(100**i))*(((100-m)**(18-i))/(100**(18-i)))
print(res1+res2-res1*res2)