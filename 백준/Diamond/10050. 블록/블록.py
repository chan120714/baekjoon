import sys
input=sys.stdin.readline

def sol(n,a):
	if n==3:
		print('2 to -1')
		print('5 to 2')
		print('3 to -3')
		return
	elif n<8:
		if n==4:
			print(a+6,'to',a-1)
			print(a+3,'to',a+6)
			print(a,'to',a+3)
			print(a+7,'to',a)
			return
		elif n==5:
			print(a+8,'to',a-1)
			print(a+3,'to',a+8)
			print(a+6,'to',a+3)
			print(a,'to',a+6)
			print(a+9,'to',a)
		elif n==6:
			print(a+10,'to',a-1)
			print(a+7,'to',a+10)
			print(a+2,'to',a+7)
			print(a+6,'to',a+2)
			print(a,'to',a+6)
			print(a+11,'to',a)
		elif n==7:
			print(a+8,'to',a-1)
			print(a+5,'to',a+8)
			print(a+12,'to',a+5)
			print(a+3,'to',a+12)
			print(a+9,'to',a+3)
			print(a,'to',a+9)
			print(a+13,'to',a)
	else:
		print(n*2-2+a,'to',a-1)
		print(a+3,'to',n*2-2+a)
		sol(n-4,a+4)
		print(a,'to',n*2-5+a)
		print(n*2-1+a,'to',a)
		
sol(int(input()),0)