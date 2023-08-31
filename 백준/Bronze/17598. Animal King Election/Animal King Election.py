l,k=0,0
for i in range(9):
    a=input()
    if a=='Lion':
        l+=1
    else:
        k+=1
if l>k:
    print("Lion")
else:
    print("Tiger")