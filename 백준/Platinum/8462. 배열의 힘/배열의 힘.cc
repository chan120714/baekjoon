#include<bits/stdc++.h>
using namespace std;
typedef long long ll;
int sqrtn;
int a[1231231],arr[1231232];
ll ret[123123];
ll res=0;

struct node{
	int l,r,num;
	
	bool operator<(node x){
		if (l/sqrtn==x.l/sqrtn) return r<x.r;
		return l/sqrtn<x.l/sqrtn;
	}
};
vector<node> tree;

void update(int x,int v){
	if (v==1){
		res-=1ll*a[x]*a[x]*x;
		a[x]+=1;
		res+=1ll*a[x]*a[x]*x;
	}
	else{
		res-=1ll*a[x]*a[x]*x;
		a[x]-=1;
		res+=1ll*a[x]*a[x]*x;
	}
	return;
}

int main(){
	cin.tie(0);cout.tie(0);
	ios::sync_with_stdio(false);
	int n,t; cin >> n >> t;
	sqrtn=sqrt(n);
	for (int i=1;i<=n;i++){
		cin >> arr[i];
	}
	int l,r;
	for (int i=0;i<t;i++){
		tree.push_back({0,0,0});
		cin >> tree[i].l >> tree[i].r;
		tree[i].num=i;
	}
	sort(tree.begin(),tree.end());
	l=tree[0].l;
	r=tree[0].l-1;
	for (int i=0;i<t;i++){
		int xl=tree[i].l,xr=tree[i].r;
		while (xl<l) update(arr[--l],1);
		while (l<xl) update(arr[l++],-1);
		while (r<xr) update(arr[++r],1);
		while (xr<r) update(arr[r--],-1);
		ret[tree[i].num]=res;
	}
	for (int i=0;i<t;i++) cout << ret[i] << '\n';
}