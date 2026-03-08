import sys
input=sys.stdin.readline
from heapq import*
from math import gcd

INF=10**18
p=[2,3,5,7,11,13,17,19,23,29,31,37,41]

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

def pri(n):
    if n in p:
        return True
    if n==1 or n%2==0:
        return False
    for k in p:
        if not mil(n,k):
            return False
    return True


for __ in range(int(input())):
    n,x=map(int,input().split())
    a=list(map(int,input().split()))

    maxa,mina=INF,1

    for i in range(2,n+1):
        if n%i:continue
        if not pri(i):continue
        x_max,x_min=INF,1

        d=[0]*i
        for j in range(n-1):
            d[(j+1)%i]+=a[j]
        d[0]+=x
        
        max_heap=[]
        min_heap=[]
        for j,v in enumerate(d):
            heappush(min_heap, (v,j))
            heappush(max_heap, (-v,j))


        def minv():
            while 1:
                v,i=min_heap[0]
                if d[i]==v:
                    return v
                heappop(min_heap)

        def maxv():
            while 1:
                v,i=max_heap[0]
                if d[i]==-v:
                    return -v
                heappop(max_heap)

        for j in range(n):
            cur_max=maxv()
            cur_min=minv()

            if cur_max*x_min<cur_min*x_max:
                x_max,x_min=cur_max,cur_min
            
            if j==n-1:
                break
            
            t=j%i
            u=(j+1)%i
            val=a[j]

            d[t]+=val-x
            d[u]+=x-val

            heappush(min_heap,(d[t],t))
            heappush(min_heap,(d[u],u))
            heappush(max_heap,(-d[t],t))
            heappush(max_heap,(-d[u],u))
        if maxa*x_min>x_max*mina:
            maxa,mina=x_max,x_min
    g = gcd(maxa, mina)
    print(maxa // g, mina // g)