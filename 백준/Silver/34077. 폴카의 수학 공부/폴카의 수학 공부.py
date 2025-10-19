for _ in' '*int(input()):
 input();a=input()
 s,t=a.find('-'),0 
 for i in range(s+2,len(a)):t=max(t,a[i]>'0')
 print('NO'*(t>0 and s!=-1)or'YES')