#include<bits/stdc++.h>
using namespace std;
const int MAX=1234;
const int INF=987654321;
int s,e;
struct edge{
	int v,c,d,r;
};
vector<edge> g[MAX];
int dis[MAX],par[MAX];
bool inq[MAX];
void makedir(int q,int w,int c,int x){
	g[q].push_back({w,x,c,g[w].size()});
	g[w].push_back({q,0,-c,g[q].size()-1});
}

bool spfa(int s,int e){
	fill(dis,dis+MAX,INF);
	memset(inq,0,sizeof(inq));
	queue<int> q;
	q.push(s);
	inq[s]=1;
	dis[s]=0;
	while (q.size()){
		int c=q.front();
		q.pop();
		inq[c]=0;
		for (int i=0;i<g[c].size();i++){
			int x=g[c][i].v;
			int k=g[c][i].c;
			if (k!=0 && dis[x]>dis[c]+g[c][i].d){
				dis[x]=dis[c]+g[c][i].d;
				par[x]=g[c][i].r;
				if (!inq[x]){
					q.push(x);
					inq[x]=1;
				}
			}
		}
	}
	return (dis[e]!=INF);
}

int main(){
	int n,m;cin >> n >> m;
	for (int i=1;i<=n;i++){
		int t;cin >> t;
		makedir(0,i,0,1);
		while (t--){
			int x,y;cin >> x >> y;
			makedir(i,n+x,y,1);
		}
	}
	s=0;
	e=n+m+1;
	for (int i=1;i<=m;i++) makedir(i+n,n+m+1,0,1);
	int cost=0,flow=0;
	while (spfa(s,e)){
		int f=INF;
		for (int x=e;x!=s;x=g[x][par[x]].v){
			edge &a=g[x][par[x]];
			f=min(f,g[a.v][a.r].c);
		}
		flow+=f;
		cost+=dis[e]*f;
		for (int x=e;x!=s;x=g[x][par[x]].v){
			edge &a=g[x][par[x]];
			a.c+=f;
			g[a.v][a.r].c-=f;
		}
	}
	cout << flow << '\n'<< cost;
}