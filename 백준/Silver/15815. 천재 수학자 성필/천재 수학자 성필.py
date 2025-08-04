
a=input()
stack=[]
for i in a:
    if '0'<=i<='9':
        stack.append(int(i))
    else:
        w=stack.pop()
        q=stack.pop()
        if i=='*':
            stack.append(w*q)
        elif i=='+':
            stack.append(w+q)
        elif i=='-':
            stack.append(q-w)
        else:
            stack.append(q//w)
print('%d'%stack[-1])