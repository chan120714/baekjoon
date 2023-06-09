#include<bits/stdc++.h>
int n(int a){
	if (a==0){
		return 0;
	}
	else{
		return n(a-1)+a;
	}
}
main(){
	int a;
	scanf("%d",&a);
	printf("%d",n(a));
}