#include<bits/stdc++.h>
using namespace std;
const int MAX=1234;
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
	int n,m;cin >> n >> m;
	vector<int> a(n),b(m);
	s=0;
	e=n+m+1;
	for (int i=0;i<n;i++) cin >> a[i];
	for (int i=0;i<m;i++) cin >> b[i];
	
	for (int i=0;i<n;i++)
	for (int j=0;j<m;j++){
		if ((a[i]<=b[j]*2 && b[j]*4<=a[i]*3) || (a[i]<=b[j] && b[j]*4<=a[i]*5)){
			makedir(i+1,n+j+1,1);
		}
	}
	for (int i=0;i<n;i++) makedir(0,i+1,1);
	for (int i=0;i<m;i++) makedir(n+i+1,n+m+1,1);
	int res=0;
	while (bfs()){
		memset(work,0,sizeof(work));
		while (1){
			int flow=dfs(s,987654231);
			if (!flow) break;
			res+=flow;
		}
	}
	cout <<res;
}