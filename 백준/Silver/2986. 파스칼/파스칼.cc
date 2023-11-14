#include<bits/stdc++.h>
using namespace std;
main(){
	cin.tie(0);
	ios::sync_with_stdio(false);
	int n,cnt=0;
	cin >> n;
	if (n==1) cout<< 0;
	else if (n%2==0) cout<< n/2;
	else if (n%3==0) cout << n/3*2;
	else if (n%5==0) cout << n/5*4;
	else if (n%7==0) cout << n/7*6;
	else if (n%11==0) cout << n/11*10;
	else if (n%13==0) cout << n/13*12;
	else if (n%17==0) cout << n/17*16;
	else if (n%19==0) cout << n/19*18;
	else if (n%23==0) cout << n/23*22;
	else{
		cnt=n/20*19;
		for (int i=n-cnt;i>=1;i--){
			if (n%i==0) break;
			cnt++;
		}
		cout<<cnt;
	}
}