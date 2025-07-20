#include<bits/stdc++.h>
using namespace std;
typedef pair<int,int> pi;
const int MAX=123456;
int sz[MAX],dep[MAX],par[MAX],top[MAX],in[MAX],out[MAX];
vector<pi> g[MAX],edge;
int tree[MAX*4];

void update(int n,int s,int e,int idx,int val){
	if (idx<s || e<idx)return;
	if (s==e){
		tree[n]=val;
		return;
	} 
	update(n*2,s,(s+e)/2,idx,val);
	update(n*2+1,(s+e)/2+1,e,idx,val);
	tree[n]=max(tree[n*2],tree[n*2+1]);
	return;
} 

int query(int n,int s,int e,int l,int r){
	if (r<s || e<l) return 0;
	if (l<=s && e<=r) return tree[n];
	return max(query(n*2,s,(s+e)/2,l,r),query(n*2+1,(s+e)/2+1,e,l,r));
}

void dfs1(int v,int last){
	sz[v]=1;
	for (auto &i:g[v]){
		if (i.first==last) continue;
		dep[i.first]=dep[v]+1;par[i.first]=v;
		dfs1(i.first,v);sz[v]+=sz[i.first];
		if (sz[i.first]>sz[g[v][0].first]) swap(i,g[v][0]);
	}
}

int pv=0;
void dfs2(int v,int last,int n){
	in[v]=++pv;
	for (auto i:g[v]){
		if (i.first==last) continue;
		if (g[v][0].first==i.first){
			top[i.first]=top[v];
		}
		else{
			top[i.first]=i.first;
		}
		dfs2(i.first,v,n);
		update(1,1,n,in[i.first],i.second);
	}
	out[v]=pv;
}

//안녕하세용 
int main(){
	cin.tie(0);cout.tie(0);
	ios::sync_with_stdio(false);
	int n;cin >> n;
	for  (int i=0;i<n-1;i++){
		int x,y,z;cin >> x>> y >> z;
		g[x].push_back({y,z});
		g[y].push_back({x,z});
		edge.push_back({x,y});
	}
	dfs1(1,-1);
	dfs2(1,-1,n);
	/*
	아 하늘에서 갑자기 HLD구현이 떨어지면 좋겠다 
	*/
	int m;cin >> m;
	while (m--){
		int x,y,z;cin >> x;
		if (x==1){
			cin >> y >>z;
			y--;
			int t1,t2;
			t1=edge[y].first;
			t2=edge[y].second;
			if (in[t1]>in[t2]) swap(t1,t2);
			update(1,1,n,in[t2],z);
		}
		else{
			cin >> y >>z;
			int t1,t2,res=0;
			t1=y;
			t2=z;
			while (top[t1]!=top[t2]){
				if (dep[top[t1]]<dep[top[t2]]) swap(t1,t2);
				res=max(res,query(1,1,n,in[top[t1]],in[t1]));
				t1=par[top[t1]];
			}
			if (in[t1]>in[t2]) swap(t1,t2);
			res=max(res,query(1,1,n,in[t1]+1,in[t2]));
			cout << res << '\n';
		}
	}
}