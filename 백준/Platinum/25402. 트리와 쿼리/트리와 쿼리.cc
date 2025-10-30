#include<bits/stdc++.h>
using namespace std;
#pragma GCC optimized("Ofast,un_looped")
#define MAX 302010
typedef long long ll;
typedef pair<ll,ll> pll;
typedef pair<int,int> pi;
vector<bool> visited(MAX);
vector<int> ist(MAX);
ll comb(ll x){
	return x*(x-1) >> 1;
}
vector<int> graph[MAX];
ll val=0,res=0;
void dfs(int x){
	if (visited[x]){
		return;
	}
	visited[x]=true;
	if (ist[x]==0){
		return;
	}
	else{
		val++;
		for (auto i:graph[x]){
			dfs(i);
		}
	}
	return;
}
int k_is_three(int a,int b,int c){
	int num=0;
	num+=graph[a][lower_bound(graph[a].begin(),graph[a].end(),c)-graph[a].begin()]==c;
	num+=graph[a][lower_bound(graph[a].begin(),graph[a].end(),b)-graph[a].begin()]==b;
	num+=graph[c][lower_bound(graph[c].begin(),graph[c].end(),b)-graph[c].begin()]==b;
	if (num==0) return 0;
	if (num==1) return 1;
	return 3;
}
int main(){
	cin.tie(0);cout.tie(0);
	ios::sync_with_stdio(false);
	int n;cin >> n;
	for (int i=1;i<n;i++){
		int x,y;
		cin >>x >> y;
		graph[x].push_back(y);
		graph[y].push_back(x);
	}
	for (int i=1;i<=n;i++){
		sort(graph[i].begin(),graph[i].end());
	}
	int m;cin >> m;
	while (m--){
		int a;
		cin >> a;
		if (a==3){
			int x,y,z;cin >>x >> y >>z;
			cout << k_is_three(x,y,z)<<'\n';
			continue;
		}
		ist.assign(n+1,0);
		visited.assign(n+1,false);
		res=0;val=0;
		for (int i=0;i<a;i++){
			int p;cin >> p;
			ist[p]=1;
		}
		for (int i=1;i<=n;i++){
			val=0;
			if (!visited[i]){
				dfs(i);
				res+=comb(val);	
			}
		}
		cout << res<<'\n';
	}
}