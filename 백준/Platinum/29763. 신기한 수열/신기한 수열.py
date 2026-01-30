N,M=map(int,input().split())
x=10**9+7
print(int(input(),2)%x if N<2else~-2**M*N*-~x//2%x)