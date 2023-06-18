#include<stdio.h>
#include<iostream>
using namespace std;
main(){
	int a=0,b,c,m=0;
	while (true){
		scanf("%d %d",&b,&c);
		a-=b;a+=c;
		m=max(m,a);
		if (c==0){
			printf("%d",m);
			break;
		}
	}
}