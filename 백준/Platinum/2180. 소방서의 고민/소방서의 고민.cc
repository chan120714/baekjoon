#include<bits/stdc++.h>
using namespace std;
typedef pair<int,int> pi;
typedef long long ll;
typedef pair<ll,ll> pll;
#define a first
#define b second

bool cmp(pll x,pll y){
	if (x.a==0 && x.b==0) return !(y.a==0 && y.b==0);
	if (y.a==0 && y.b==0) return 0;
	
	if (x.a==0) return 0;
	if (y.a==0) return 1;
	
	if  (x.b*y.a!=x.a*y.b){
		return x.b*y.a<x.a*y.b;
	}
	return x.a<y.a;
}


int main(){
	cin.tie(0);cout.tie(0);
	ios::sync_with_stdio(false);
	
	int n;cin >> n;
	vector<pll> v(n);
	
	for (int i=0;i<n;i++) cin >> v[i].a >> v[i].b;
	sort(v.begin(),v.end(),cmp);
	
	ll t=0;
	
	for (int i=0;i<n;i++){
		t=((1ll+v[i].a)%40000*t+v[i].b)%40000;
	}
	cout << t;
}