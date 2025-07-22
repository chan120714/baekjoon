#include<bits/stdc++.h>
using namespace std;
typedef long long ll;
int n,k,sqrtn;
vector<ll> a(123421),res(124231);
int tree[270000],MAX;
vector<int> v;

void update(int n,int s,int e,int idx,int v){
	while (idx<=131231){
		tree[idx]+=v;
		idx+=idx&-idx;
	}
	return;
}

ll query(int n,int s,int e,int l,int r){
	int ret=0;
	while (r>0){
		ret+=tree[r];
		r-=r&-r;
	}
	l-=1;
	while (l>0){
		ret-=tree[l];
		l-=l&-l;
	}
	return ret;
}

struct qq{
	int st,ed,num;
	bool operator <(qq &x){
		if (st/sqrtn==x.st/sqrtn) return ed<x.ed;
		return st/sqrtn<x.st/sqrtn;
	}
};

int ist(int a){
	return upper_bound(v.begin(),v.end(),a)-v.begin();
}

ll l,r,cur;

void l_pl(){
	cur-=query(1,1,MAX,1,a[l]-1);
	update(1,1,MAX,a[l],-1);
	l++;
}

void l_mi(){
	l--;
	cur+=query(1,1,MAX,1,a[l]-1);
	update(1,1,MAX,a[l],1);
}

void r_pl(){
	r++;
	cur+=query(1,1,MAX,a[r]+1,MAX);
	update(1,1,MAX,a[r],1);
}

void r_mi(){
	cur-=query(1,1,MAX,a[r]+1,MAX);
	update(1,1,MAX,a[r],-1);
	r--;
}

int main(){
	cin.tie(0);cout.tie(0);
	ios::sync_with_stdio(false);
	cin >> n >> k;
	sqrtn=sqrt(n);
	vector<qq> t;
	v.push_back(0);
	v.push_back(0);
	v.push_back(1234567890);
	for (int i=1;i<=n;i++){
		cin >> a[i];
		v.push_back(a[i]);
	}
	sort(v.begin(),v.end());
	for (int i=1;i<=n;i++){
		a[i]=lower_bound(v.begin(),v.end(),a[i])-v.begin()+1;
	}
	MAX=v.size()+100;
	for (int i=0;i<k;i++){
		ll x,y;
		cin >> x >> y;
		t.push_back({x,y,i});
	}
	sort(t.begin(),t.end());
	l=t[0].st;r=l-1;
	for (int i=0;i<k;i++){
		while (t[i].st<l) l_mi();
		while (t[i].st>l) l_pl();
		while (t[i].ed<r) r_mi();
		while (t[i].ed>r) r_pl();
		res[t[i].num]=cur;
	}
	for (int i=0;i<k;i++){
		cout << res[i]<<'\n';
	}
}