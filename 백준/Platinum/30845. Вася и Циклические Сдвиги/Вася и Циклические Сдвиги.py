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
n=input()
t=len(n)-fail(n)[-1]
if len(n)%t==0:
    print(len(n)//t)
else:
    print(1)