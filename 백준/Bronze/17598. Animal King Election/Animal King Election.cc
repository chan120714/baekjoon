#include<bits/stdc++.h>
using namespace std;
int a,b;
main(){
	char s[20];
	while (scanf("%s",s)!=EOF){
		if (s[0]=='T'){a++;}
		else{b++;}
		s[20];
	}
	if (a>b){
		printf("Tiger");
	}
	else{
		printf("Lion");
	}
}