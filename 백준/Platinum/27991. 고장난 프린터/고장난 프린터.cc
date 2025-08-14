#include<bits/stdc++.h>
using namespace std;
typedef long long ll;
ll tree[5000000];

void update(int n,int s,int e,int i,ll v){
	if (i<s || e<i) return;
	if (s==e){
		tree[n]=v;
		return;
	}
	update(n*2,s,(s+e)/2,i,v);
	update(n*2+1,(s+e)/2+1,e,i,v);
	tree[n]=tree[n*2]+tree[n*2+1];
	return;
}

int query(int n,int s,int e,int l,int r){
	if (r<s || e<l) return 0;
	if (l<=s && e<=r) return tree[n];
	return query(n*2,s,(s+e)/2,l,r)+query(n*2+1,(s+e)/2+1,e,l,r);
}
int main(){
	cin.tie(0);cout.tie(0);
	ios::sync_with_stdio(false);
	ll n,m,ret=0;int res=0;cin >> n >> m;
	vector<ll> a(n+1);
	vector<pair<ll,int> > b;
	for (int i=1;i<=n;i++){
		cin >> a[i];
		b.push_back({a[i],i});
	}
	sort(b.begin(),b.end());
	for (auto i:b){
		update(1,1,n,i.second,1);
		ll v=i.first;
		int cur=query(1,1,n,1,min(m/v,n));
		if (m/v<n)cur+=(m%v>=a[m/v+1] ? 1 : 0);
		if (res<cur){
			res=cur;
			ret=v;
		}
	}
	cout << ret;
}