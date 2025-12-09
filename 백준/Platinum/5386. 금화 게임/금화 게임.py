for _ in' '*int(input()):
    s,k=map(int,input().split())
    if k%2:print(s%2)
    else:print(k if s%-~k==k else s%-~k%2)