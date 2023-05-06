from decimal import *

getcontext().prec = 100
getcontext().rounding = ROUND_HALF_UP

a,b,c=map(Decimal,map(int,input().split()))
l,h=(c-b)/a,(c+b)/a
pi=Decimal('3.1415926535897932384626433832795028841971693993751058209749445923078164062862089986280348253421170679')
m=(l+h)/2

def sin(x):
    x%=(2*pi)
    getcontext().prec += 2
    i, lasts, s, fact, num, sign = 1, 0, x, 1, x, 1
    while s != lasts:
        lasts = s
        i += 2
        fact *= i * (i-1)
        num *= x * x
        sign *= -1
        s += num / fact * sign
    getcontext().prec -= 2
    return +s

while h-l>Decimal('1e-60'):
     m=(l+h)/2
     if a*m+b*sin(m)-c>Decimal('1e-60'):
        h=m
     else:
        l=m
print(round(h,6))