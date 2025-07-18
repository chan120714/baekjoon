#include<bits/stdc++.h>
using namespace std;
typedef long long ll;

ll a[123456],b[123456];

const ll MAX= 2147483647;

struct node{
	ll len;
	ll maxc,rc,lc;
}tree[412341];

node merge(node a,node b){
	if (b.len==0) return a;
	if (a.len==0) return b;
	
	node x;
	x.len=a.len+b.len;
	
	if (a.len==a.maxc) x.lc=a.len+b.lc;
	else x.lc=a.lc;
	
	if (b.len==b.maxc) x.rc=b.len+a.rc;
	else x.rc=b.rc;
	
	x.maxc=max({a.maxc,b.maxc,b.lc+a.rc});
	return x;
}

node init(int n,int s,int e){
    if (s==e){
    	int k = b[s]==0 ? 1: 0;
		return tree[n]={1,k,k,k};
    }
	int m=(s+e)/2;
    return tree[n]=merge(init(n*2,s,m),init(n*2+1,m+1,e));
}

node lazy(int n,int s,int e,ll v){
	if (s==e){
    	int k = b[s]==0 ? 1: 0;
		return tree[n]={1,k,k,k};
	}
	if (v<=(s+e)/2) lazy(n*2,s,(s+e)/2,v);
	else lazy(n*2+1,(s+e)/2+1,e,v);
	return tree[n]=merge(tree[n*2],tree[n*2+1]);
}

void update(int n,int s,ll v){
	if (s<2 || s>n-1) return;
	b[s]+=v;
	lazy(1,2,n-1,s);
} 

node query(int n,int s,int e,int l,int r){
	if (e<l || r<s) return {0,0,0,0};
	if (l<=s && e<=r) return tree[n];
	node L=query(n*2,s,(s+e)/2,l,r),R=query(n*2+1,(s+e)/2+1,e,l,r);
	return merge(L,R);
}

int main(){
	cin.tie(0);cout.tie(0);
	ios::sync_with_stdio(false);
	int n;cin >>n;
	for (int i=1;i<=n;i++) cin >> a[i];
	for (int i=2;i<=n-1;i++) b[i]=a[i-1]+a[i+1]-2*a[i];
	init(1,2,n-1);
	int m;cin >> m;
	while (m--){
		int t,i,j;cin >> t >> i >> j;
		if (t==1){
			int x,y;cin>>x >> y;
			update(n,i-1,x);
			update(n,i,-x+y);
			update(n,j,-x-(j-i+1)*y);
			update(n,j+1,x+(j-i)*y);
		}
		else{
			if (j-i<2) cout << j-i+1 << '\n';
			else cout << query(1,2,n-1,i+1,j-1).maxc+2 << '\n';
		} 
	}
}