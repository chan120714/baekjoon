n,a,b=map(int,input().split())
for i in range(1,9-n):
    m,k=map(int,input().split())
    if m+k>6:
        a+=min(6,m)*3
        b+=6*3
    else:
        a+=m*3
        b+=(m+k)*3
if a>=66 and b>=130:
    print("Nice")
else:
    print("Nae ga wae")