#include<bits/stdc++.h>
using namespace std;
int dp[1050][200],s[1020],h[1010];
int main(){
	cin.tie(0);cout.tie(0);
	ios::sync_with_stdio(false);
	int n,k;cin >> n>> k;
	for (int i=1;i<=n;i++) cin >> s[i];
	for (int i=1;i<=n;i++) cin >> h[i];
	for (int i=1;i<=n;i++){
		for (int j=0;j<=100;j++){
			int minv=min(j+k,100);
			if (minv>=h[i]){
				dp[i][minv-h[i]]=max(dp[i][minv-h[i]],dp[i-1][j]+s[i]);
			}
			dp[i][minv]=max(dp[i][minv],dp[i-1][j]);
		}
	}
	int res=0;
	for (int i=0;i<=100;i++) res=max(res,dp[n][i]);
	cout << res;
}
/*
kpsc 파이팅
*/