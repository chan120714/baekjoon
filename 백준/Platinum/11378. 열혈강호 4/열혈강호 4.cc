#include<bits/stdc++.h>
using namespace std;
const int MAX=2311;
const int INF=987654321;
int level[MAX],work[MAX];
int s,e;
struct edge{
	int v,c,r;
};
vector<edge> g[MAX];

void makedir(int q,int w,int x){
	g[q].push_back({w,x,g[w].size()});
	g[w].push_back({q,0,g[q].size()-1});
}
bool bfs(){
	memset(level,0,sizeof(level));
	level[s]=1;
	queue<int> q;
	q.push(s);
	while (q.size()){
		int t=q.front();
		q.pop();
		for (auto i:g[t]){
			if (i.c==0 || level[i.v]) continue;
			level[i.v]=level[t]+1;
			q.push(i.v);
		}
	}
	return level[e];
}

int dfs(int x,int c){
	if (x==e) return c;
	for (;work[x]<g[x].size();work[x]++){
		edge &t=g[x][work[x]];
		if (level[x]+1==level[t.v] && t.c>0){
			int v=dfs(t.v,min(t.c,c));
			if (v){
				t.c-=v;
				g[t.v][t.r].c+=v;
				return v;
			}
		}
	}
	return 0;
}

int main(){
	cin.tie(0);cout.tie(0);
	ios::sync_with_stdio(false);
	int n,m,k;
	cin >> n >> m >> k;
	for (int i=1;i<=n;i++){
		int t;cin >> t;
		makedir(0,i,1);
		makedir(n+m+2,i,INF);
		while (t--){
			int a; cin >> a;
			makedir(i,a+n,1);
		}
	}
	makedir(0,n+m+2,k);
	for (int i=n+1;i<=n+m;i++) makedir(i,n+m+1,1);
	e=n+m+1;
	s=0;
	int res=0;
	while (bfs()){
		memset(work,0,sizeof(work));
		while (1){
			int flow=dfs(s,INF);
			if (!flow) break;
			res+=flow;
		}
	}
	cout << res;
}