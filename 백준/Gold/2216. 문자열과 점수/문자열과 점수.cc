#include<bits/stdc++.h>
using namespace std;
int lcs[3001][3001];
int main(){
	cin.tie(0);cout.tie(0);
	ios::sync_with_stdio(false);
	int n,m,k,z,x;
	string a,b;
	cin >> n >> m >> k;
	cin >>a >> b;
	z=a.size();x=b.size();
	for (int i=0;i<3001;i++){
		lcs[i][0]=i*m;
		lcs[0][i]=i*m;
	}
	for (int i=1;i<=z;i++)
	for (int j=1;j<=x;j++){
		if (a[i-1]==b[j-1]) lcs[i][j]=lcs[i-1][j-1]+n;
		else lcs[i][j]=max(lcs[i-1][j-1]+k,max(lcs[i-1][j],lcs[i][j-1])+m);
	}
	cout << lcs[z][x];
}