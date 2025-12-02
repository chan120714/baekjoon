from fractions import*
while True:
    try:
        n=input()
        if not n.isdecimal():
            continue
        n=int(n)
        if n==1:
            print(1)
        elif n==2:
            print(3)
        else:
            a=Fraction(1,1)
            for i in range(2,n+1):
                a+=Fraction(1,i)
            a*=n
            i=int(a.numerator)
            j=int(a.denominator)
            k=i//j
            i%=j
            print(' '*len(str(k)),i)
            print(k,'-'*len(str(j)))
            print(' '*len(str(k)),j)
    except EOFError:
        break
