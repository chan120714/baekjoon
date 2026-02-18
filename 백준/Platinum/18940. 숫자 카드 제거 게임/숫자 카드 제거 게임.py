for i in' '*int(input()):
 n=int(input())
 print("Platina"if(n%2<1 and(n in[4,8,14,20,24,28,34,38,42]or(n>42 and(n-42)%34 in[0,12,16,20,30])))else"Yuto")