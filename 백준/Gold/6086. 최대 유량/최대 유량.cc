#include<bits/stdc++.h>
using namespace std;
const int MAX=123;

int level[MAX],work[MAX];
int s=1,e=26;
struct edge{
	int v,c,r;
};
vector<edge> g[MAX];

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
int find(char x){
	if (x<='Z') return x-'A'+1;
	return x-'a'+27;
}

int main(){
	cin.tie(0);cout.tie(0);
	ios::sync_with_stdio(false);
	int n;
	cin >> n;
	for (int i=0;i<n;i++){
		char a,b;int x;
		cin >> a >> b >> x;
		int q=find(a),w=find(b);
		g[q].push_back({w,x,g[w].size()});
		g[w].push_back({q,0,g[q].size()-1});
		g[q].push_back({w,0,g[w].size()});
		g[w].push_back({q,x,g[q].size()-1});
	}
	int res=0;
	while (bfs()){
		memset(work,0,sizeof(work));
		while (1){
			int flow=dfs(s,987654231);
			if (!flow) break;
			res+=flow;
		}
	}
	cout << res;
}