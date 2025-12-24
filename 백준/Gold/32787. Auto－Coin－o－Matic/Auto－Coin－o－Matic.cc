#include<bits/stdc++.h>
using namespace std;

int dp[120312];

int main(){
	cin.tie(0);cout.tie(0);
	ios::sync_with_stdio(false);
	int n,m;cin >> n >> m;
	unordered_set<int> a;
	
	for (int i=0;i<n;i++){
		int x;cin >> x;
		a.insert(x);
	}
	
	
	vector<pair<int,int> > q;
	
	for (int i=0;i<m;i++){
		char x;
		int y;
		cin >> x >> y;
		if (x=='Q'){
			q.push_back({0,y});
		}
		else{
			q.push_back({1,y});
			a.erase(y);
		}
	}
	reverse(q.begin(),q.end());
	
	for (int i=1;i<=100000;i++){
		dp[i]=-1;
	}
	for (auto i:a){
		for (int j=i;j<=100000;j++){
			if (dp[j-i]>=0){
				if (dp[j]==-1) dp[j]=dp[j-i]+1;
				else dp[j]=min(dp[j-i]+1,dp[j]);
			}	
		}
	}
	vector<int> c;
	for (auto i:q){
		if (i.first==0){
			c.push_back(dp[i.second]);
		}
		else{
			for (int j=i.second;j<=100000;j++){
				if (dp[j-i.second]>=0){				
					if (dp[j]==-1) dp[j]=dp[j-i.second]+1;
					else dp[j]=min(dp[j-i.second]+1,dp[j]);
				}
			}
		}
	}
	reverse(c.begin(),c.end());
	for (auto i:c) cout << i << '\n';
	
}