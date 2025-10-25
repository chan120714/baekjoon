#include<bits/stdc++.h>
using namespace std;
#define ll long long

struct xg{
	ll x,y;
};
xg xgcd(ll n,ll m){
	if (m==0) return {1,0};
    xg t=xgcd(m,n%m);
    return {t.y,t.x-(n/m)*t.y};
}
ll gcd(ll a,ll b) {
    return b ? gcd(b, a%b) : a;
}

int main(){
	int a;
	cin >> a;
	while (a--){
		ll n,m,k,rev=0;
		cin >>n >> m;
		if (n==1 && m==1){
			cout << 2 <<'\n';
			continue;
		}
		if (n==1){
			cout << 1<<'\n';
			continue;
		}
		if (m==1){
			if (n+1>1000000000) cout << "IMPOSSIBLE\n";
			else cout << n+1 << '\n';
			continue;
		}
		if (gcd(n,m)!=1){
			cout<<"IMPOSSIBLE\n";
			continue;
		}
		xg pp=xgcd(m,n);
		ll t=pp.x%n;
		t+=n;
		t%=n;
		if (t>1000000000) cout << "IMPOSSIBLE\n";
		else cout << t << '\n';
	}
}
