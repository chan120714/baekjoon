#include<bits/stdc++.h>
using namespace std;
typedef long long ll;
typedef pair<int,int> pi;
typedef pair<ll,ll> pll;
const int MAX=523456;

ll sz[MAX],dep[MAX],par[MAX],top[MAX],in[MAX],out[MAX];
vector<ll> g[MAX];
ll tree[MAX*4],plus1[MAX*4];

void lazy(int n,int s,int e){
	if (plus1[n]==0) return;
	tree[n]+=(e-s+1)*plus1[n];
	if (s!=e){
		plus1[n*2]+=plus1[n];
		plus1[n*2+1]+=plus1[n];
	}
	plus1[n]=0;
	return;
}
void update_p(int n,int s,int e,int l,int r,ll val){
	lazy(n,s,e);
	if (r<s || e<l)return;
	if (l<=s && e<=r){
		plus1[n]+=val;
		lazy(n,s,e);
		return;
	} 
	update_p(n*2,s,(s+e)/2,l,r,val);
	update_p(n*2+1,(s+e)/2+1,e,l,r,val);
	tree[n]=tree[n*2]+tree[n*2+1];
	return;
} 


ll query(int n,int s,int e,int l,int r){
	lazy(n,s,e);
	if (r<s || e<l) return 0;
	if (l<=s && e<=r) return tree[n];
	return query(n*2,s,(s+e)/2,l,r)+query(n*2+1,(s+e)/2+1,e,l,r);
}

void dfs1(int v,int last){
	sz[v]=1;
	for (auto &i:g[v]){
		if (i==last) continue;
		dep[i]=dep[v]+1;par[i]=v;
		dfs1(i,v);sz[v]+=sz[i];
		if (sz[i]>sz[g[v][0]]) swap(i,g[v][0]);
	}
}

int pv=0;
void dfs2(int v,int last,int n){
	in[v]=++pv;
	for (auto i:g[v]){
		if (i==last) continue;
		if (g[v][0]==i){
			top[i]=top[v];
		}
		else{
			top[i]=i;
		}
		dfs2(i,v,n);
	}
	out[v]=pv;
}

//안녕하세용 
int main(){
	cin.tie(0);cout.tie(0);
	ios::sync_with_stdio(false);
	int n,c;cin >> n >> c;
	for  (int i=0;i<n-1;i++){
		int x,y,z;cin >> x>> y;
		g[x].push_back(y);
		g[y].push_back(x);
	}
	dfs1(c,-1);
	top[c]=c;
	dfs2(c,-1,n);
	int m;cin >>m;
	while (m--){
		ll x,y,z;cin >> x;
		if (x==1){
			ll a;cin >> y;
			ll t1,t2,res=0;
			t1=y;
			t2=c;
			a=1;
			while (top[t1]!=top[t2]){
				if (dep[top[t1]]<dep[top[t2]]) swap(t1,t2);
				update_p(1,1,n,in[top[t1]],in[t1],a);
				t1=par[top[t1]];
			}
			if (in[t1]>in[t2]) swap(t1,t2);
			update_p(1,1,n,in[t1],in[t2],a);
		}
		else{
			cin >> y;
			ll t1,t2,res=0;
			t1=y;
			t2=y;
			res=query(1,1,n,in[t1],in[t2]);
			ll kv=dep[y]+1;
			cout << res*kv << '\n';
		}
	}
}