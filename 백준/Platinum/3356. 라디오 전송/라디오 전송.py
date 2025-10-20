def fail(s):
    n=len(s)
    a=[0]*n
    st=0
    for i in range(1,n):
        while (st and s[i]!=s[st]):
            st=a[st-1]
        if s[st]==s[i]:
            st+=1
            a[i]=st
    return a

def kmp(a,b):
    n=len(a)
    m=len(b)
    s=fail(b)
    res=[]
    st=0
    for i in range(n):
        while (st and a[i]!=b[st]):
            st=s[st-1]
        if a[i]==b[st]:
            if st+1==m:
                res.append(i-st+1)
                st=s[st]
            else:
                st+=1
    return res

n=int(input())
k=fail(input())
print(n-k[-1])