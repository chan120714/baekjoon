#include<bits/stdc++.h>
using namespace std;
int lcs[1001][1001];
int main(){
	string a,b;
	cin >> a >> b;
	int n=a.size(),m=b.size();
	for (int i=0;i<1001;i++){
		lcs[i][0]=i;
		lcs[0][i]=i;
	}
	for (int i=1;i<=n;i++)
	for (int j=1;j<=m;j++){
		if (a[i-1]==b[j-1]) lcs[i][j]=lcs[i-1][j-1];
		else lcs[i][j]=min(lcs[i-1][j-1],min(lcs[i-1][j],lcs[i][j-1]))+1;
	}
	cout << lcs[n][m];
}