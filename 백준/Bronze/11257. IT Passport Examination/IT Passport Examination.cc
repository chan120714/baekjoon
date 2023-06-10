#include<bits/stdc++.h>
using namespace std;
main(){
	int a,b,c,d,e;
	scanf("%d",&e);
	for (int i=0;i<e;i++){
		scanf("%d %d %d %d",&a,&b,&c,&d);
		if (b+c+d>=55 && b>=11 && c>=8 && d>=12){
			printf("%d %d PASS\n",a,b+c+d);
		}
		else{
			printf("%d %d FAIL\n",a,b+c+d);
		}
	}
}