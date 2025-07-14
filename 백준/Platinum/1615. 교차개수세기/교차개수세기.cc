#include<bits/stdc++.h>
using namespace std;
int tree[550000];

void update(int n,int s,int e,int idx,int x){
	if (idx<s || e<idx) return;
	if (s==e){
		tree[n]+=1;
		return;
	}
	update(n*2,s,(s+e)/2,idx,x);
	update(n*2+1,(s+e)/2+1,e,idx,x);
	tree[n]=tree[n*2]+tree[n*2+1];
	return;
}

int query(int n,int s,int e,int l,int r){
	if (l<=s && e<=r) return tree[n];
	if (s>r || e<l) return 0;
	return query(n*2,s,(s+e)/2,l,r)+query(n*2+1,(s+e)/2+1,e,l,r);
}

int main(){
	cin.tie(0);cout.tie(0);
	ios::sync_with_stdio(false);
	int n,m;cin >> n >> m;
	long long res=0;
	vector<pair<int,int>> a(m); 
	for (int i=0;i<m;i++) cin >> a[i].first >> a[i].second;
	sort(a.begin(),a.end());
	for (int i=0;i<m;i++){
		res+=query(1,1,n,a[i].second+1,n);
		update(1,1,n,a[i].second,1);
	}
	cout << res;
}