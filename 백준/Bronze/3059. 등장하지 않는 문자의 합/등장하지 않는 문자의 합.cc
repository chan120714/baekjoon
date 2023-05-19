#include<bits/stdc++.h>
using namespace std;
main(){
	int a[26],b;
	char c[1000];
	scanf("%d",&b);
	int s;
	for (int i=0;i<b;i++){
		s=0;
		for (int j=0;j<26;j++){
			a[j]=0;
		}
		for (int j=0;j<1000;j++){
			c[j]='0';
		}
		scanf("%s",c);
		for (int j=0;j<1000;j++){
			a[int(c[j])-65]=1;
		}
		for (int j=0;j<26;j++){
			if (a[j]==0){
				s+=(j+65);
			}
		}
		printf("%d\n",s);
	}
}