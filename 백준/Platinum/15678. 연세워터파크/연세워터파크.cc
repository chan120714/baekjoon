#include<bits/stdc++.h>
using namespace std;
typedef long long ll;
ll tree[512312];

void update(int n,int s,int e,int i,ll v){
	if (i<s || e<i) return;
	if (s==e){
		tree[n]=v;
		return;
	}
	update(n*2,s,(s+e)/2,i,v);
	update(n*2+1,(s+e)/2+1,e,i,v);
	tree[n]=max(tree[n*2],tree[n*2+1]);
}

ll query(int n,int s,int e,int l,int r){
	if (e<l || r<s) return LLONG_MIN;
	if (l<=s && e<=r) return tree[n];
	return max(query(n*2,s,(s+e)/2,l,r),query(n*2+1,(s+e)/2+1,e,l,r));
}

int main(){
	cin.tie(0);cout.tie(0);
	ios::sync_with_stdio(false);
	int n,d;cin >>n >> d;
	for (int i=1;i<=n;i++){
		ll x;cin >> x;
		update(1,0,n,i,max(0ll,query(1,0,n,max(0,i-d),i-1))+x);
	}
	cout << query(1,0,n,1,n);
}