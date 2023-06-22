n,m,k=map(int,input().split())
r=(n**2/(m**2+k**2))**(1/2)
a=m*r
b=k*r
print(int(a),int(b))