n=int(input())
if n%9==0:
    k=n//9-1
    print('9'+'9'*k)
    print('36'+'9'*k)
    print('27'+'9'*k)
elif n%9==1:
    k=n//9-1
    print('19'+'9'*k)
    print('55'+'9'*k)
    print('73'+'9'*k)
else:print(-1)