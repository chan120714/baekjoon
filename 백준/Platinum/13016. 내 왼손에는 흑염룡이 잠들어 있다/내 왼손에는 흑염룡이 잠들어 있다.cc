#include<bits/stdc++.h>
using namespace std;
int val,dist,res[51021];
vector<pair<int,int> > g[51231];
void dfs(int x,int lst,int d){
	if (dist<d){
		dist=d;
		val=x;
	}
	res[x]=max(res[x],d);
	for (auto i:g[x]){
		if (i.first!=lst){
			dfs(i.first,x,d+i.second);
		}
	}
	return;
}
int main(){
	cin.tie(0);cout.tie(0);
	ios::sync_with_stdio(false);
	int n;cin >> n;
	for (int i=1;i<n;i++){
		int x,y,d;cin >>x >> y >> d;
		g[x].push_back({y,d});
		g[y].push_back({x,d});
	}
	dfs(1,-1,0);
	dist=0;
	dfs(val,-1,0);
	dfs(val,-1,0);
	for (int i=1;i<=n;i++){
		cout << res[i] <<'\n';
	}
}