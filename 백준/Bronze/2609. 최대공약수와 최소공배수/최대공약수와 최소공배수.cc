#include<bits/stdc++.h>
using namespace std;
int gcd(int a,int b){
	if (a>b){
		int c;
		c=a;a=b;b=c;
	}
	if (b%a==0){
		return a;
	}
	else{
		return gcd((b%a),a);
	}
}
main(){
	cin.tie(0);
	ios::sync_with_stdio(false);
	int a,b;
	cin>>a>>b;
	cout<<gcd(a,b)<<"\n"<<a*(b/gcd(a,b));	
}