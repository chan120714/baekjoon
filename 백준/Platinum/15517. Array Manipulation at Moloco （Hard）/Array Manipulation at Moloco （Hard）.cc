#include<bits/stdc++.h>
using namespace std;
typedef long long ll;

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

int main(){
	cin.tie(0);cout.tie(0);
	ios::sync_with_stdio(false);
	int n;cin >> n;
	vector<int> a(n),b(n);
	
	for (int i=0;i<n;i++) {
		cin >> a[i];
		b[i]=a[i];
	}
	Fenwick Tree(n);
	sort(b.begin(),b.end());
	
	for (auto i:a){
		cout << Tree.query(1,lower_bound(b.begin(),b.end(),i)-b.begin()+1) <<'\n';
		Tree.update(lower_bound(b.begin(),b.end(),i)-b.begin()+1,1);
	}
}