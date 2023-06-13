#include<bits/stdc++.h>
using namespace std;
main(){
	long long a,b;
	scanf("%lld",&a);
	b=1+4*a+3*a*(a-1)/2;b%=45678;
	printf("%lld",b);
}