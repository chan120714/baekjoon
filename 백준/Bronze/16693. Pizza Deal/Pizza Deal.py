import math
a,b=map(int,input().split())
c,d=map(int,input().split())
print('Slice of pizza'if b/a<d/(c**2*math.pi)else'Whole pizza')
