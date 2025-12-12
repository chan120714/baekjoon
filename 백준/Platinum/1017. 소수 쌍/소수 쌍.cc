#include<bits/stdc++.h>
using namespace std;
int visited[1023],ist[1023],prime[2012];
vector<int> graph[1023];
vector<int> res;

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
	int n,m;
	
	for (int i=2;i<=2010;i++){
		int ist=1;
		for (int j=2;j<i;j++){
			if (i%j==0) ist=0;
		}
		if (ist==1){
			prime[i]=1;
		}
	}
	
	
	cin >> n;
	vector<int> a(n);
	for (int i=0;i<n;i++) cin >> a[i];
	for (int x=1;x<n;x++){
		if (prime[a[0]+a[x]]==0) continue;
		int ret=0;
		for (int i=1;i<n;i++){
			if (i==x) continue;
			for (int j=1;j<n;j++){
				if (j==x) continue;
				
				if (prime[a[i]+a[j]]==1){
					graph[i].push_back(j);
				}
			}
		}
		for (int i=1;i<n;i++){
			fill(ist,ist+51,0);
			if (dfs(i)) ret++;
		}
		if (ret==n-2){
			res.push_back(a[x]);
		}
		for (int i=1;i<n;i++){
			ist[i]=0;
			visited[i]=0;
			while (graph[i].size()){
				graph[i].pop_back();
			}
		}
	}
	sort(res.begin(),res.end());
	if (res.size()==0){
		cout << -1;
	}
	else{
		for (auto i:res){
			cout << i << ' ';
		}
	}
}