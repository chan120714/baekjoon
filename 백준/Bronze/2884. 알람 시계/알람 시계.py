a,b=map(int,input().split())
h=(1395+a*60+b)%1440
print(f'{h//60} {h%60}')