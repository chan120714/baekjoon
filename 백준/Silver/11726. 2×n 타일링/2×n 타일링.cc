#include<bits/stdc++.h>
using namespace std;
int a[1011],n;
main(){
	scanf("%d",&n);
	a[1]=1;
	a[2]=2;
	for (int i=3;i<1001;i++){
		a[i]=(a[i-1]+a[i-2])%10007;
	}
	printf("%d",a[n]);
}