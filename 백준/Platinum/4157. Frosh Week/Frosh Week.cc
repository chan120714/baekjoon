#include<bits/stdc++.h>
using namespace std;
typedef long long ll;

const int MAX=2097153;
struct Fenwick{
	int n;
	vector<ll> a;
	Fenwick(int n_=0){
		n=n_;
		a.assign(n+1,0);
	}
	void update(int x,ll v){
		while (x<=n){
			a[x]+=v;
			x+=x&-x;
		}
		return;
	}
	ll q(int x){
		ll res=0;
		while (x){
			res+=a[x];
			x-=x&-x;
		}
		return res;
	}
	ll query(int x,int y){
		return q(y)-q(x-1);
	}
	
};

ll a[1823481];
void sol(){
	int n;cin >> n;
	Fenwick Tree(MAX);
	vector<int> a(n),b(n);
	for (int i=0;i<n;i++) {
		cin >> a[i];
		b[i]=a[i];
	}
	sort(b.begin(),b.end());
	ll res=0;
	for (auto i:a){
		int x=lower_bound(b.begin(),b.end(),i)+1-b.begin();
		Tree.update(x,1);
		res+=Tree.query(x+1,n);
	}
	cout << res <<'\n';
}
int main(){
	cin.tie(0);cout.tie(0);
	ios::sync_with_stdio(false);
	int T=1;
	for (int i=1;i<=T;i++){
		sol();
	}
}