#include<bits/stdc++.h>
using namespace std;
typedef long long ll;
typedef pair<ll,ll> pll;
const int MAX=123456;
ll tree[MAX*4],a[MAX],lazy[MAX*4];

int init(int n,int s,int e){
	if (s==e) return tree[n]=a[s]-a[s-1];
	return tree[n]=init(n*2,s,(s+e)/2)+init(n*2+1,(s+e)/2+1,e);
}
void lazyp(int n,int s,int e){
	if (lazy[n]){
		tree[n]+=(e-s+1)*lazy[n];
		if (s^e){
			lazy[n*2]+=lazy[n];
			lazy[n*2+1]+=lazy[n];
		}
		lazy[n]=0;
	}
	return; 
}
ll update(int n,int s,int e,int l,int r,ll v){
	lazyp(n,s,e);
	if (r<s || e<l) return tree[n];
	if (l<=s && e<=r){
		lazy[n]=v;
		lazyp(n,s,e);
		return tree[n];
	}
	return tree[n]=update(n*2,s,(s+e)/2,l,r,v)+update(n*2+1,(s+e)/2+1,e,l,r,v);
}

ll query(int n,int s,int e,int l,int r){
	lazyp(n,s,e);
	if (r<s || e<l) return 0;
	if (l<=s && e<=r) return tree[n];
	return query(n*2,s,(s+e)/2,l,r)+query(n*2+1,(s+e)/2+1,e,l,r);
}

int main(){
	cin.tie(0);cout.tie(0);
	ios::sync_with_stdio(false);
	int n;cin >> n;
	for (int i=1;i<=n;i++) cin >> a[i];
	n+=1;
	init(1,1,n);
	int m;cin >> m;
	while (m--){
		int a,b,c;cin >> a >> b;
		if (a==1){
			cin >> c;
			update(1,1,n,b,c,1);
			update(1,1,n,c+1,c+1,-c+b-1);
		}
		else{
			cout << query(1,1,n,1,b) << '\n';
		}
	}
}