#include<bits/stdc++.h>
using namespace std;
int visited[1023],ist[1023];
vector<int> graph[1023];
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
			graph[i].push_back(y);
		}
	}
	for (int i=1;i<=n;i++){
		fill(ist,ist+1023,0);
		if (dfs(i)) res++;
	}
	cout << res;
    }