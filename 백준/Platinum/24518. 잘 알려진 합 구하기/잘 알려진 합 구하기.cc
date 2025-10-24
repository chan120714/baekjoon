#include<bits/stdc++.h>
using namespace std;
typedef long long ll;
ll m;
const ll MOD=1'000'000'007;
ll f(ll s,ll e){
	ll res=0;
	if (s/m == e/m){
		e%=m;
		s%=m;
		return e*(e+1)/2-s*(s-1)/2;
	}
	res=(e/m-s/m-1)*(m*(m-1)/2);
	s%=m;
	e%=m;
	res+=m*(m-1)/2-s*(s-1)/2;
	res+=e*(e+1)/2;
	return res%MOD;
}
ll double_count(ll n){
	ll i,j,res=0;
	for (i=1;i<=n;i=j+1){
		j=n/(n/i);
		res+=(n/i)*f(i,j);
		res%=MOD;
	}
	return res%MOD;
}
int main(){
	ll n;
	cin >> n >> m;
	cout << double_count(n);
}