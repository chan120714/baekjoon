#include<bits/stdc++.h>
using namespace std;
typedef long long ll;
int n,k,sqrtn;
vector<ll> a(223421),res(224231);
int MAX,tree[270000],cnt[223456],s=0;
vector<int> v;

void update(int idx,int v){
	if (v>0){
		cnt[tree[idx]]-=1;
		tree[idx]+=1;
		cnt[tree[idx]]+=1;
		s=max(s,tree[idx]);
	}
	else{
		cnt[tree[idx]]-=1;
		tree[idx]-=1;
		cnt[tree[idx]]+=1;
		while (s && cnt[s]==0) s-=1;
	}
	return;
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

int main(){
	cin.tie(0);cout.tie(0);
	ios::sync_with_stdio(false);
	cin >> n >> k;
	sqrtn=sqrt(n);
	vector<qq> t;
	for (int i=1;i<=n;i++){
		cin >> a[i];
	}
	for (int i=1;i<=n;i++){
		a[i]+=100001;
	}
	cnt[0]=213415;
	for (int i=0;i<k;i++){
		ll x,y;
		cin >> x >> y;
		t.push_back({x,y,i});
	}
	sort(t.begin(),t.end());
	l=t[0].st;r=l-1;
	for (int i=0;i<k;i++){
		while (t[i].st<l) update(a[--l],1);
		while (t[i].ed>r) update(a[++r],1);
		while (t[i].st>l) update(a[l++],-1);
		while (t[i].ed<r) update(a[r--],-1);
		res[t[i].num]=s;
	}
	for (int i=0;i<k;i++){
		cout << res[i]<<'\n';
	}
}