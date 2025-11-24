import sys
input=sys.stdin.readline
M=10**9+7

def f(st,ed):
    x=(ed-st+1)*(ed-st+2)//2
    x-=1
    return x%M


for __ in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    res=0
    t=[0]*301021
    v=[0]*(n+1)
    st=0
    for i in range(n):
        t[a[i]]+=1
        if t[a[i]]>1:
            while t[a[i]]>1:
                t[a[st]]-=1
                if st==0:
                    res+=i-st-1
                    st+=1
                    #print(st,res)
                    continue
                res=(res+(pow(st+1,i-st+1,M)-1)*pow(st,-1,M)-st-2)%M
                st+=1
                #print(st,res)
        v[i]=st
    for i in range(n):
        if i==0:
            if st==0:res+=n-v[i]-1
            #print(i,res)
            continue
        res=(res+(pow(i+1,i-v[i]+2,M)-1)*pow(i,-1,M)-i-2)%M
        if i>=st:res=(res+(pow(i+1,n-i+1,M)-1)*pow(i,-1,M)-i-2)%M
        #print(i,res)
    print(res)
