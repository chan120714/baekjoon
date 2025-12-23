#include<bits/stdc++.h>
using namespace std;
typedef unsigned long long ll;
typedef pair<ll,ll> pll;

pll dp[100][100][100];

int main(){
	int n,K;cin >> n >> K;

    for (int i=0;i<100;i++)
    for (int j=0;j<100;j++)
    for (int k=0;k<100;k++) dp[i][j][k]={0,1};

    dp[0][0][0]={1,1};
	for (int i=1;i<=n;i++)
	for (int j=0;j<=K;j++)
	for (int k=0;k+j<=i;k++){
		ll f=0,s=1;
		
		for (int x=1;x<=i;x++) s*=3;
		 
		if (i-(j+k)<K && j!=K){ // lose 
            f+=s/dp[i-1][j][k].second/3*dp[i-1][j][k].first;	
		}
		// win
        if (j>=1){
            f+=s/dp[i-1][j-1][k].second/3*dp[i-1][j-1][k].first;
            
        }
		// draw
		if (j!=K && k>=1){
			f+=s/dp[i-1][j][k-1].second/3*dp[i-1][j][k-1].first;
        }
        
        dp[i][j][k]={f,s};
	}
	ll f=0,s=1;
	
	for (int x=1;x<=n;x++) s*=3;
		
	for (int i=1;i<=n;i++)
	for (int j=0;j<=n;j++){
		f+=s/dp[i][K][j].second*dp[i][K][j].first;
	}
	ll t=gcd(f,s);
	cout << f/t << ' ' << s/t;
}