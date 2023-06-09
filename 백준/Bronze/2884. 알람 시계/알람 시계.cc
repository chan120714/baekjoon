#include<bits/stdc++.h>
using namespace std;
main(){
	int a,b;
	scanf("%d %d",&a,&b);
	int c=0;
	c+=(a*60)+b+1395;
	c%=1440;
	printf("%d %d",c/60,c%60);
}