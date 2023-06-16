#include<stdio.h>
main(){
	int a[100001],n,m,k,l,sum;
	scanf("%d %d",&n,&m);
	for (int i=1;i<=n;i++){
		scanf("%d",&k);
		a[i]=k+a[i-1];
	}
	for (int i=0;i<m;i++){
		scanf("%d %d",&k,&l);
		printf("%d\n",a[l]-a[k-1]);
	}
}