#include<bits/stdc++.h>
using namespace std;
const int MAX=2560;
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
	int T;cin >> T;
	while (T--){
		int n,m,ret=0;cin >> n >> m;
		int a[100][100];
		for (int i=0;i<n;i++)
		for (int j=0;j<m;j++){
			cin >> a[i][j];
			ret+=a[i][j];
		}
		
		for (int i=0;i<n;i++)
		for (int j=0;j<m;j++){
			if ((i+j+1)%2){
				makedir(0,i*m+j+1,a[i][j]);
				if (j+1<m) makedir(1+i*m+j,1+i*m+j+1,INF);
				if (i+1<n) makedir(1+i*m+j,1+(i+1)*m+j,INF);
				if (j>0) makedir(1+i*m+j,1+i*m+j-1,INF);
				if (i>0) makedir(1+i*m+j,1+(i-1)*m+j,INF);
			}
			else{
				makedir(1+i*m+j,n*m+1,a[i][j]);
			}
		}
		s=0;
		e=n*m+1;
		int res=0;
		while (bfs()){
			memset(work,0,sizeof(work));
			while (1){
				int flow=dfs(s,987654231);
				if (!flow) break;
				res+=flow;
			}
		}
		cout << ret-res << '\n';
		for (int i=0;i<MAX;i++) g[i].clear();
	}
}