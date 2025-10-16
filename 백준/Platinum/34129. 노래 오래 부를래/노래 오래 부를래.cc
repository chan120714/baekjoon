#include<bits/stdc++.h>
using namespace std;

int dp[120312];
int main(){
	int n,k;cin >> n >> k;
	vector<pair<int,int> > a(n);
	for (int i=1;i<=n;i++){
		cin >> a[i-1].first;
		a[i-1].second=i;
	}
	if (n==1){
		cout << 1 << ' ' << a[0].first  << '\n';
		cout << 1;
		return 0;
	}
	sort(a.begin(),a.end());
	if (a[0].first>k-1){
		cout << 1 << ' ' << a[n-1].first << '\n';
		cout << a[n-1].second ;
		return 0;;
	}
	for (int i=0;i<n-1;i++){
		if (a[i].first>k)continue;
		for (int j=k;j>=a[i].first;j--){
			if (!dp[j-a[i].first])continue;
			dp[j]=max(dp[j-a[i].first]+1,dp[j]);
		}
		dp[a[i].first]=max(1,dp[a[i].first]);
	}
	int res=0,ret=0;
	for(int i=k-1;i>=0;i--){
		if (dp[i]){
			res=i;
			cout << dp[i]+1 << " " << i+a[n-1].first << '\n';
			ret=a[n-1].second;
			break;
		}
	}
	for (int i=n-2;i>=0;i--){
		if ((res-a[i].first)>=0 && dp[res]-dp[res-a[i].first]==1){
			cout << a[i].second << ' ';
			res-=a[i].first;
			//cout << res <<' ' << a[i].first << '\n';
		}
	}
	cout << ret;
}