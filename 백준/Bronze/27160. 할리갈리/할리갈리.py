from collections import defaultdict

n=int(input())
d=defaultdict(int)

for i in range(n):
    s,x=input().split()
    d[s]+=int(x)

print("YES" if 5 in d.values() else "NO")
