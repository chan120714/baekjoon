#include<bits/stdc++.h>
using namespace std;
typedef long long ll;
#define cost first.first 
#define x1 first.second 
#define x2 second.first 
#define va second.second.first
#define t second.second.second 
typedef pair<pair<ll,ll>,pair<ll,pair<ll,ll> > > plll;
int parent[54312],res[123123],cur[123123];

int find(int x){
	if (parent[x]==x) return x;
	return find(parent[x]);
}

void unioned(int x,int y){
	x=find(x);
	y=find(y);
	if (x>y) swap(x,y);
	parent[x]=parent[y];
}

struct graph{
	ll u,v,w,x,y,tt;
};vector<graph> g;

int main(){
	cin.tie(0);cout.tie(0);
	ios::sync_with_stdio(false);
	int n,m,b;cin >> n >>m >> b;
	for (int i=0;i<m;i++){
		g.push_back({0,0,0,0,0,i+1});
		cin >> g[i].u >> g[i].v >> g[i].w >> g[i].x >> g[i].y;
	}
	ll st=1,ed=100000100000;
	ll ret=1;
	while (st<=ed){
		ll mid=(st+ed+1)/2,val=0;
		for (int i=1;i<=n;i++) parent[i]=i;
		for (int i=1;i<=m;i++) cur[i]=0;
		priority_queue<plll, vector<plll>, greater<plll> > q;
		for (auto i:g){
			plll curv;
			curv.x1=i.u;
			curv.x2=i.v;
			curv.cost=max(0ll,(mid-i.w+i.x-1)/i.x*i.y);
			curv.va=max(0ll,(mid-i.w+i.x-1)/i.x);
			curv.t=i.tt;
			q.push(curv);
		}
		while (q.size()){
			if (find(q.top().x1)==find(q.top().x2)){
				q.pop();
				continue;
			}
			unioned(q.top().x1,q.top().x2);
			cur[q.top().t]=q.top().va;
			val+=q.top().cost;
			q.pop();
		}
		if (val<=b){
			ret=mid;
			for (int i=1;i<=m;i++) res[i]=cur[i];
			st=mid+1;
		}
		else{
			ed=mid-1;
		}
	}
	cout << ret  << '\n';
	for (int i=1;i<=m;i++){
		cout << res[i] <<'\n';
	}
}