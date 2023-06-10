#include<bits/stdc++.h>
using namespace std;
main(){
	int a,b[5],c=0;
	scanf("%d",&a);
	for (int i=0;i<5;i++){
		scanf("%d",&b[i]);
	}
	for (int j=0;j<5;j++){
		if (a==b[j]){
			c+=1;
		}
	}
	printf("%d",c);
}