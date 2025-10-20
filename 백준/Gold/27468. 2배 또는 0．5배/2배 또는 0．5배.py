n=int(input())
print("YES",*[x+b'#!""'[(x-n%2)%4]%3for x in range(n)])