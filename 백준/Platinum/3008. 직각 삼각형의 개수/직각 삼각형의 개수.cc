#include<bits/stdc++.h>
using namespace std;
typedef long long ll;
ll x[2000],y[2000],d[2000][2000];
bool f(ll x1,ll x2,ll x3){
    ll s=x1+x2+x3;
    if (x1*2==s || x2*2==s || x3*2==s){return 1;}
    return 0;
}
int main(){
	cin.tie(0);cout.tie(0);
	ios::sync_with_stdio(false);
	
	int n;cin >> n;

	for (int i=0;i<n;i++){
		cin >> x[i] >> y[i];
	}
	
    for (int a=0;a<n-1;a++)
    for (int b=a+1;b<n;b++){
        d[a][b]=(x[a]-x[b])*(x[a]-x[b])+(y[a]-y[b])*(y[a]-y[b]);
    }
	int res=0;
	
	for (int i=0;i<n-2;i++)
	for (int j=i+1;j<n-1;j++)
	for (int k=j+1;k<n;k++){
        res+=f(d[i][j],d[j][k],d[i][k]);
	}
	cout << res;
}