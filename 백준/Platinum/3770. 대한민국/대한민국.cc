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
	int n,m,k;cin >>n >> m >> k;
	Fenwick Tree(m);
	vector<pair<int,int> > a(k);
	for (int i=0;i<k;i++){
		cin >> a[i].first >> a[i].second;
	}
	sort(a.begin(),a.end());
	ll res=0;
	for (auto i:a){
		Tree.update(i.second,1);
		res+=Tree.query(i.second+1,m);
	}
	cout << res <<'\n';
}
int main(){
	cin.tie(0);cout.tie(0);
	ios::sync_with_stdio(false);
	int T;cin >> T;
	for (int i=1;i<=T;i++){
		cout << "Test case " <<i<<": ";
		sol();
	}
}