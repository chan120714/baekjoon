#include<bits/stdc++.h>
using namespace std;
int visited[2023],ist[2023];
vector<int> graph[2023];
bool dfs(int x){
	for (auto i:graph[x]){
		if (ist[i]) continue;
		ist[i]=1;
		if (visited[i]==0 || dfs(visited[i])){
			visited[i]=x;
			return true;
		}
	}
	return false;
}
int main(){
	cin.tie(0);cout.tie(0);
	ios::sync_with_stdio(false);
	int n,m,k,res=0;
	cin >> n >> m >> k;
	for (int i=1;i<=n;i++){
		int x;
		cin >> x;
		while (x--){
			int y;
			cin >> y;
			graph[i].push_back(y);
			graph[i+n].push_back(y);
		}
	}
	for (int i=1;i<=n;i++){
		fill(ist,ist+2023,0);
		if (dfs(i)) res++;
	}
	int ret=0;
	for (int i=n+1;i<=2*n;i++){
		fill(ist,ist+2023,0);
		if (dfs(i)) ret++;
	}
	cout << res+min(ret,k);
}