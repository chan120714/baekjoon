a=int(input())
b=input()
for i in range(len(b)):
    print(a*int(b[-1-i]))
print(a*int(b))
