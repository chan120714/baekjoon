#include<iostream>
#include<vector>
#include<algorithm>
#include<queue>
using namespace std;
typedef long long ll;
typedef pair<int,int> pi;
typedef pair<ll,ll> pll;
const ll INF=60000000;
ll visit_cnt[54],plus_val[55],dist[55];
bool visited[55],cycle[56];
vector<pll> graph[55];
bool bfs(int st,int ed){
	queue<int>q;
	q.push(st);
	int vis[55];
	for (int i=0;i<55;i++) vis[i]=0;
	vis[st]=1;
	while (q.size()){
		int x=q.front();q.pop();
		for (auto i:graph[x]){
			if (!vis[i.first]){
				vis[i.first]=true;
				q.push(i.first);
			}
		}
	}
	return vis[ed];
}
int main(){
	cin.tie(0);cout.tie(0);
	ios::sync_with_stdio(false);
	queue<int> q;
	ll n,st,ed,m,ist=1;
	cin >> n >> st >> ed >> m;
	for (int i=0;i<m;i++){
		ll x,y,z;
		cin >> x >> y >> z;
		graph[x].push_back({y,z});
	}
	for (int i=0;i<n;i++){
		cin >> plus_val[i];
		visited[i]=false;
		dist[i]=INF;
	}
	q.push(st);
	visit_cnt[st]++;
	dist[st]=-plus_val[st];
	if (!bfs(st,ed)){
		cout << "gg";
		return 0;
	}
	while (q.size()){
		ll x=q.front();q.pop();
		visited[x]=false;
		for (auto i:graph[x]){
			ll dis=i.second-plus_val[i.first]+dist[x];
			if (dis>=dist[i.first]) continue;
			dist[i.first]=dis;
			if (visited[i.first]) continue;
			visit_cnt[i.first]++;
			if (visit_cnt[i.first]>m*2){
				if (bfs(i.first,ed)){
					cout << "Gee";
					return 0;
				}
				else{
					visited[i.first]=true;cycle[i.first]=true;
					continue;
				}
			}
			q.push(i.first);
			visited[i.first]=true;
		}
	}
	for (int i=0;i<n;i++){
		if (cycle[i] && bfs(i,ed)){
			cout << "Gee";
			return 0;
		}
	}
	cout << -dist[ed];
}