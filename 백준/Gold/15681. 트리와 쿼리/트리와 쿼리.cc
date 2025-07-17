#include<bits/stdc++.h>
using namespace std;
vector<int> graph[123412];
int res[123456];
int dfs(int x,int pre){
	for (auto i:graph[x]){
		if (i!=pre){
			res[x]+=dfs(i,x);
		}
	}
	return res[x]+=1;
}

int main(){
	cin.tie(0);cout.tie(0);
	ios::sync_with_stdio(false);
	int n,r,q;cin >>n >> r >> q;
	for (int i=1;i<n;i++){
		int u,v;cin >> u >> v;
		graph[u].push_back(v);
		graph[v].push_back(u);
	}
	dfs(r,-1);
	while (q--){
		int u;cin >> u;
		cout << res[u] <<'\n';
	}
}