#include<bits/stdc++.h>
using namespace std;
int visited[1023],ist[1023];
vector<int> graph[1023];
const int INF=987654321;
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
int g[250][250];
int main(){
	cin.tie(0);cout.tie(0);
	ios::sync_with_stdio(false);
	int k,c,m,res=INF;
	cin >> k >> c >> m;
	for (int i=1;i<=k+c;i++){
		for (int j=1;j<=k+c;j++){
			cin >> g[i][j];
			if (!g[i][j]) g[i][j]=INF;
		}
	}
	
	for (int a=1;a<=k+c;a++){
		for (int i=1;i<=k+c;i++){
			for (int j=1;j<=k+c;j++){
				g[i][j]=min(g[i][j],g[i][a]+g[a][j]);
			}
		}
	}
	
	int st=1,ed=50000;
	while (st<=ed){
		int mid=st+ed>>1;
		for (int i=k+1;i<=k+c;i++)
		for (int j=1;j<=k;j++){
			if (g[i][j]<=mid){
				for (int a=1;a<=m;a++){
					graph[i-k].push_back(m*(j-1)+a);
				}
			}
		}
		
		int res1=0;
		for (int i=1;i<=c;i++){
			fill(ist,ist+1023,0);
			if (dfs(i)) res1++;
		}
		
		for (int i=1;i<=c;i++) graph[i].clear();
		
		if (res1==c){
			res=min(res,mid);
			ed=mid-1;
		}
		else{
			st=mid+1;
		}
		fill(visited, visited+1023, 0);
	}
	
	cout << res;
}