import sys
input=sys.stdin.readline
 
n=int(input())
a=[input().rstrip() for i in range(n)]
 
a.reverse()
 
cur=a[0]
for i in a[1:]:
    if cur[0]=='T':
        if i[0]=='T':
            pass
        else:
            cur='LIE'
    else:
        if i[0]=='T':
            cur='LIE'
        else:
            cur="TRUTH"
print(cur)