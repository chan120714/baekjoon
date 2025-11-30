#include<bits/stdc++.h>
using namespace std;
const int MAX=252034;
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

int ga[512][512];
int main(){
	cin.tie(0);cout.tie(0);
	ios::sync_with_stdio(false);
	int n,it=0;cin >> n;
    for (int i=1;i<=n;i++)
    for (int j=1;j<=n;j++){
        cin >> ga[i][j];
        if (ga[i][j]==0) it+=1;
    }
	for (int i=1;i<=n;i++)
    for (int j=1;j<=n;j++){
        if (ga[i][j]==0) {
            makedir(i*n+j,n*n+3*n+1,1);
            makedir(n*n+n+i,i*n+j,1);
            makedir(n*n+n*2+j,i*n+j,1);
        }
        if (ga[i][j]>1){
            makedir(0,i*n+j,ga[i][j]-1);
            makedir(i*n+j,n*n+n+i,INF);
            makedir(i*n+j,n*n+2*n+j,INF);
        }
    }
	int res=0;
	e=n*n+3*n+1;
	s=0;
	
	while (bfs()){
		memset(work,0,sizeof(work));
		int flow;
        while (flow=dfs(s,INF)){
            res+=flow;
        }
	}
	cout << res+2*(it-res);
}