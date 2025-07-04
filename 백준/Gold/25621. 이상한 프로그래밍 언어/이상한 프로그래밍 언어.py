import sys
input=sys.stdin.readline
n,k=map(int,input().split())
a=0
for i in range(n):
    q,w=map(str,input().split())
    if q[0]=='+':
        type1=0
    elif q[0]=='-':
        type1=1
    else:
        type1=2
    if w[0]=='+':
        type2=0
    elif w[0]=='-':
        type2=1
    else:
        type2=2
    q=int(q[1:])
    w=int(w[1:])
    if type1==0:
        if type2==0:
            k+=max(q,w)
        elif type2==1:
            k+=q
        else:
            if k+q>=k*w and a==0:
                k+=q
            elif a and w<=1:
                k+=q
            else:
                if a:
                    a=min(a*w,333212)
                k*=w
    elif type1==1:
        if type2==1:
            k-=min(q,w)
            if a==0 and k<0:
                k=0
            elif k<0:
                a-=1
                k+=1000000007
        elif type2==0:
            k+=w
        else:
            if w==0:
                k-=q
                if a==0 and k<0:
                    k=0
                elif k<0:
                    a-=1
                    k+=1000000007
            else:
                if a:
                    a=min(a*w,313212)
                k*=w
    else:
        if type2==2:
            if a and max(q,w)!=1:
                a=min(a*max(q,w),313212)
            k*=max(q,w)
        elif type2==0: 
            if k*q<=k+w and a==0:
                k+=w
            elif a and q<=1:
                k+=w
            else:
                if a:
                    a=min(a*q,313212)
                k*=q
        else:
            if q==0:
                k-=w
                if k<0 and a==0:
                    k=0
                elif k<0:
                    a-=1
                    k+=1000000007
            else:
                if a and q!=1:
                    a=min(a*q,313212)
                k*=q
    a+=k//1000000007
    k%=1000000007
print(k)
