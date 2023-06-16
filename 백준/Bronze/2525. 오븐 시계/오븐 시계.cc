#include<stdio.h>
main(){
	int a,b,c,d=0;
	scanf("%d %d %d",&a,&b,&c);
	d+=a*60+b+c;
	d%=1440;
	printf("%d %d",d/60,d%60);
}