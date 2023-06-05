a=int(input())
for i in range(a):
    for j in range(a):
        k=i//3
        p=j//3
        if k%3==1 and p%3==1:
            print(' ',end='')
        elif i%3==1 and j%3==1:
            print(' ',end='')
        else:
            if i//9%3==1 and j//9%3==1:
                print(' ',end='')
            elif i//27%3==1 and j//27%3==1:
                print(' ',end='')
            elif i//81%3==1 and j//81%3==1:
                print(' ',end='')
            elif i//243%3==1 and j//243%3==1:
                print(' ',end='')
            elif i//729%3==1 and j//729%3==1:
                print(' ',end='')
            elif i//2187%3==1 and j//2187%3==1:
                print(' ',end='')
            elif i//6561%3==1 and j//6561%3==1:
                print(' ',end='')
            else:
                print("*",end='')
    print()