n=int(input())

k=(~-n).bit_length()
print(k)
for j in range(k):
    a=[i for i in range(1,-~n) if (~-i if 1<<k==n else i)>>j&1]
    print(len(a),*a)
