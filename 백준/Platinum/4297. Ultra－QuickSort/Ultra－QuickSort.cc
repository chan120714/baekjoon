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

void sol(int n){
	vector<int> a(n),b(n),c(n+1);
	for (int i=0;i<n;i++){
		cin >> a[i];
		b[i]=a[i];
	}
	sort(b.begin(),b.end());
	for (int i=0;i<n;i++){
		c[lower_bound(b.begin(),b.end(),a[i])-b.begin()+1]=i+1;
	}
	Fenwick Tree(n);
	ll res=0;
	for (int i=1;i<=n;i++){
		res+=c[i]-Tree.query(1,c[i])-1;
		Tree.update(c[i],1);
	}
	cout << res << '\n';
}
int main(){
	cin.tie(0);cout.tie(0);
	ios::sync_with_stdio(false);
	while (1){
		int n;cin >> n;
		if (n==0)break;
		sol(n);
	}
}