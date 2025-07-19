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
	int n,m,res=0;
	cin >> n >> m;
	for (int i=1;i<=n;i++){
		int x;
		cin >> x;
		while (x--){
			int y;
			cin >> y;
			graph[i*2-1].push_back(y);
			graph[i*2].push_back(y);
		}
	}
	for (int i=1;i<=n*2;i++){
		fill(ist,ist+2023,0);
		if (dfs(i)) res++;
	}
	cout << res;
}