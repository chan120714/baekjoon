#include<bits/stdc++.h>
using namespace std;
typedef long long ll;
const ll MOD=1'000'000'007;
ll tree[12][170000];

void update(int a,int n,int s,int e,int i,ll v){
	while (i<=130000){
		tree[a][i]+=v;
		i+=i&-i;
	}
	return;
}

ll query(int a,int n,int s,int e,int l,int r){
	ll res=0;
	while (r){
		res+=tree[a][r];
		r-=r&-r;
	}
	return res%MOD;
}
int main(){
	cin.tie(0);cout.tie(0);ios::sync_with_stdio(false);
	int n;cin >> n;
	vector<int> a(n);
	for (int i=0;i<n;i++) cin >> a[i];
	for (auto i:a){
		for (int j=2;j<=11;j++){
			update(j,1,1,n,i,query(j-1,1,1,n,1,i-1));
		}
		update(1,1,1,n,i,1);
	}
	cout << query(11,1,1,n,1,n);
}