#include<iostream>
using namespace std;
typedef long long ll;
ll sol(ll x,ll y,ll k){
	ll res=0;
	while (x!=y){
		if (x>y){
			x=(x+k-2)/k;
			res+=1;
		}
		else{
			y=(y+k-2)/k;
			res+=1;
		}
	}
	return res;
}
int main(){
	cin.tie(0);cout.tie(0);
	ios::sync_with_stdio(false);
	ll n,m,k;
	cin >> n >> m >> k;
	for (int i=0;i<k;i++){
		ll a,b;
		cin >> a >> b;
		if (m==1){
			cout << abs(a-b)<<'\n';
			continue;
		}
		cout << sol(a,b,m)<<'\n';
	}
}