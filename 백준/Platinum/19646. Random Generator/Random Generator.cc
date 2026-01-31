#include<bits/stdc++.h>
using namespace std;
typedef long long ll;
typedef pair<ll,ll> pll;

ll tree[654321];

void update(int x,ll v){
	while (x<=200000){
		tree[x]+=v;
		x+=x&-x;
	}
	return;
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

ll kth(ll k){
	int i=0,pw=131072;
	for (int j=pw;j>0;j>>=1){
		int nx=i+j;
		if (nx<=200000 && tree[nx]<k){
			k-=tree[nx];
			i=nx;
		}
	}
	return i+1;
}


int main(){
	cin.tie(0);cout.tie(0);
	ios::sync_with_stdio(false);
	
	int n;cin >> n;
	vector<ll> w(n+1),p(n+1),res;
	
	
	for (int i=1;i<=n;i++){
		ll x;cin >> x;
		w[i]=x;
		update(i,w[i]);
	}
	
	for (int i=1;i<=n;i++){
		cin >> p[i];
	}

	for (int i=1;i<=n;i++){
		int j=kth(p[i]);
		res.push_back(j);
		update(j,-w[j]);
		w[j]=0;
	}
	
	for (int i=0;i<n;i++){
		cout << res[i] << ' ';
	}
}