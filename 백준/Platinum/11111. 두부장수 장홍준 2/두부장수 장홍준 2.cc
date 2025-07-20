#include<bits/stdc++.h>
using namespace std;
const int MAX=2650;
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
int cost[6][6]={10,8,7,5,0,1,8,6,4,3,0,1,7,4,3,2,0,1,5,3,2,2,0,1,0,0,0,0,0,0,1,1,1,1,0,0};

int main(){
	int n,m;cin >> n >> m;
	char a[123][123];
	for (int i=0;i<n;i++)
	for (int j=0;j<m;j++){
		cin >> a[i][j];
	}
	
	for (int i=0;i<n;i++){
		for (int j=0;j<m;j++){
			if ((i+j+1)%2){
				makedir(0,i*m+j+1,0,1);
				if (j+1<m) makedir(1+i*m+j,1+i*m+j+1,-cost[a[i][j]-'A'][a[i][j+1]-'A'],1);
				if (i+1<n) makedir(1+i*m+j,1+(i+1)*m+j,-cost[a[i][j]-'A'][a[i+1][j]-'A'],1);
				if (j>0) makedir(1+i*m+j,1+i*m+j-1,-cost[a[i][j]-'A'][a[i][j-1]-'A'],1);
				if (i>0) makedir(1+i*m+j,1+(i-1)*m+j,-cost[a[i][j]-'A'][a[i-1][j]-'A'],1);
			}
			makedir(0,i*m+j+1,0,1);
			makedir(1+i*m+j,n*m+1,0,1);
		}
	}
	s=0;
	e=n*m+1;
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
	cout << -cost;
}