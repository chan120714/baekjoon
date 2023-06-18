#include<stdio.h>
main(){
	int a=1,n,m,k;
	scanf("%d",&k);
	for (int i=0;i<k;i++){
		scanf("%d %d",&n,&m);
		if (n==a){
			a=m;
		}
		else if (m==a){
			a=n;
		}
	}
	printf("%d",a);
}