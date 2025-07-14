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
	int T;cin >> T;
	while (T--){
		int n;cin >> n;
		long long res=0;
		vector<int> a(n+1),dp(n+1),ret(n+1);
		for (int i=1;i<=n;i++){
			int x;cin >> x;
			a[x]=i;
			ret[i]=x;
		}
		for (int i=1;i<=n;i++){
			int x;cin >> x;
			dp[a[x]]=i;
		}
		for (int i=1;i<=n;i++){
			res+=query(1,1,n,dp[a[ret[i]]],n);
			update(1,1,n,dp[a[ret[i]]],1);
		}
		cout << res << '\n';
		for (int i=0;i<550000;i++) tree[i]=0;
	}
}