import sys
input=sys.stdin.readline
sys.setrecursionlimit(100000)
from math import *
from random import*
p=[2,3,5,7,11,13,17,19,23,29,31,37,41]


#분할정복 함수
def pow(x,y,p):
    if y<2:
        return (x**y)%p
    if y%2:
        return (pow(x,y//2,p)**2*x)%p
    return (pow(x,y//2,p)**2)%p

#밀러 라빈
def mil(n,a):
    s,d=0,n-1
    while d%2==0:
        s+=1
        d//=2
    x=pow(a,d,n)
    if x==1 or x+1==n:
        return True
    for i in range(s-1):
        x=pow(x,2,n)
        if x+1==n:
            return True
    return False

def pri(n):#소수 판별
    if n in p:
        return True
    if n==1 or n%2==0:
        return False
    for k in p:
        if not mil(n,k):
            return False
    return True

def rho(n):#폴라드 로
    if pri(n):
        return n
    if n==1:
        return 1
    if n%2==0:
        return 2
    x,c,d=randint(2,n-1),randint(1,n-1),1
    y=x
    while d==1:
        x=(x**2+c)%n
        y=(y**2+c)%n
        y=(y**2+c)%n
        d=gcd(n,abs(x-y))
        if d==n:
            return rho(n)
    if pri(d):
        return d
    return rho(d)


dp=[0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181, 6765, 10946, 17711, 28657, 46368, 75025, 121393, 196418, 317811, 514229, 832040, 1346269, 2178309, 3524578, 5702887, 9227465, 14930352, 24157817, 39088169, 63245986, 102334155, 165580141, 267914296, 433494437, 701408733, 1134903170, 1836311903, 2971215073, 4807526976, 7778742049, 12586269025, 20365011074, 32951280099, 53316291173, 86267571272, 139583862445, 225851433717, 365435296162, 591286729879, 956722026041, 1548008755920, 2504730781961, 4052739537881, 6557470319842, 10610209857723, 17167680177565, 27777890035288, 44945570212853, 72723460248141, 117669030460994, 190392490709135, 308061521170129, 498454011879264, 806515533049393, 1304969544928657, 2111485077978050, 3416454622906707, 5527939700884757, 8944394323791464, 14472334024676221, 23416728348467685, 37889062373143906, 61305790721611591, 99194853094755497, 160500643816367088, 259695496911122585, 420196140727489673, 679891637638612258, 1100087778366101931, 1779979416004714189, 2880067194370816120, 4660046610375530309, 7540113804746346429, 12200160415121876738, 19740274219868223167]

def f(x):
    t=log2(x)
    t*=10**7
    t=int(t)
    f=t//10
    if t%10>=5:
        f+=1
    print('%d.%.6d'%(f//1000000,f%1000000))

def g(x):
    res=[]
    while x>1:
        f=rho(x)
        res.append(f)
        x//=f
    res.sort()
    return res
lines = sys.stdin.readlines()
for line in lines:
    x,y=map(str,line.split())
    x=int(x.lower(),16)
    y=int(y.lower(),16)
    if x>=y:
        break
    print(f'Range {x} to {y}:') 
    ist=0
    for i in range(len(dp)):
        if dp[i]<x:continue
        if dp[i]>y:break
        ist=1
        if (dp[i]==0):
            print('Fib(0) = 0, lg does not exist')
        else:
            print(f'Fib({i}) = {dp[i]}, lg is ',end='')
            f(dp[i])
        if dp[i]<2:
            print("No prime factors")
        else:
            print('Prime factors:',*g(dp[i]))
    if ist==0:
        print('No Fibonacci numbers in the range')
    print()