#include<stdio.h>
main(){
	unsigned long long n,sum=0;
	scanf("%d",&n);
	for (int i=0;i<n;i++){
		sum+=n*i+i;
	}
	printf("%lld",sum);
}