#include<bits/stdc++.h>
using namespace std;
typedef long long ll;
ll tree[123456];

void update(int x){
	while (x<=100000){
		tree[x]+=1;
		x+=x&-x;
	}
}
ll q(int x){
	ll res=0;
	while (x){
		res+=tree[x];
		x-=x&-x;
	}
	return res;
}

ll query(int x,int y){
	return q(y)-q(x-1);
}

void sol(int n){
	fill(tree,tree+123456,0);
	unordered_map<string,int> mp;
	
	for (int i=1;i<=n;i++){
		string x;
		cin >> x;
		mp[x]=i;
	}
	ll res=0;
	for (int i=1;i<=n;i++){
		string a;cin >> a;
		int x=mp[a];
		res+=query(x+1,n);
		update(x);
	}
	cout << res << '\n';
}
int main(){
	cin.tie(0);cout.tie(0);
	ios::sync_with_stdio(false);
	
	while (1){
		int x;cin >> x;
		if (x==0) break;
		sol(x);
	}
}