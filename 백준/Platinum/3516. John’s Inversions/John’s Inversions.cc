#include<bits/stdc++.h>
using namespace std;
typedef long long ll;

int tree[123412];

void update(int x){
	while (x<=123123){
		tree[x]+=1;
		x+=x&-x;
	}
}
int q(int x){
	int res=0;
	while(x){
		res+=tree[x];
		x-=x&-x;
	}
	return res;
}
int query(int x,int y){
	return q(y)-q(x-1);
}
int main(){
	cin.tie(0);cout.tie(0);
	ios::sync_with_stdio(false);
	int n;cin >> n;
	vector<pair<int,int> > a(n);
	vector<int> b(n);
	for (int i=0;i<n;i++){
		cin >> a[i].first >> a[i].second;
		b[i]=a[i].second;
	
	}
	sort(a.begin(),a.end());
	sort(b.begin(),b.end());
	
	ll res=0;
	for (int i=0;i<n;i++){
		ll v=upper_bound(b.begin(),b.end(),a[i].second)-b.begin()+1;
		res+=i-q(v);
		update(v);
		
	}
	cout << res;
}