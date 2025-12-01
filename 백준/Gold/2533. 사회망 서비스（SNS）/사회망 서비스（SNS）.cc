#include<bits/stdc++.h>
using namespace std;
#pragma GCC optimized("Ofast,un_looped")
typedef long long ll;
vector<int> graph[1234567];
int dp[1234567][2];
/* 
0-> 얼리 아답터 
1-> 아님 
*/
void dfs(int last,int x){
	int val0=0,val1=0;
	for (auto i:graph[x]){
		if (i!=last){
			dfs(x,i);
			val0+=min(dp[i][1],dp[i][0]);
			val1+=dp[i][0];
		}
	}
	val0+=1;
	dp[x][0]=val0;
	dp[x][1]=val1;
	return;
}
int main(){
	cin.tie(0);cout.tie(0);
	ios::sync_with_stdio(false);
	int n;cin >> n;
	for (int i=1;i<n;i++){
		int x,y;cin >> x >> y;
		graph[x].push_back(y);
		graph[y].push_back(x);
	}
	dfs(-1,1);
	cout << min(dp[1][0],dp[1][1]);
}