#import<cstdio>
int x,n;main(){puts("YES");for(scanf("%d",&n);x<n;)printf("%d ","1201"[(++x-n%2)%4]-49+x);}