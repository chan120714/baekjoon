#include<bits/stdc++.h>
using namespace std;

vector<int> Z(string &s){
	int n=s.size();
	vector<int> z(n);
	z[0]=n;
	
	int l=0,r=0;
	for (int i=1;i<n;i++){
		if (i<=r){
			z[i]=min(r-i+1,z[i-l]);
		}
		while (i+z[i]<n && s[z[i]]==s[i+z[i]]){
			z[i]++;
		}
		if (i+z[i]-1>r){
			l=i;
			r=i+z[i]-1;
		}
	}
	return z;
}

int f(int x,int i,vector<int> &z){
	if (i>=z.size()) return 1;
	if (z[i]<x){
		if (z[i]+i==z.size()) return 1;
		return 0;
	}
	return f(x,i+x,z);
}
int main(){
	cin.tie(0);cout.tie(0);
	ios::sync_with_stdio(false);
	int n,m;cin >>n >> m;
	string s;cin >>s;
	auto z=Z(s);
	int res=0;
	if (n<=m) res=n;
	for (int i=1;i<n;i++){
		if ((n%i==0 || i-n%i<=m) && f(i,i,z)){
			res=max(res,i);
		}
	}
	cout << res;
}