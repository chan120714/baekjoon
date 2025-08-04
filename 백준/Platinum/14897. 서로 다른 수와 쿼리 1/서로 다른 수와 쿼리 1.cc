#include<bits/stdc++.h>
#pragma GCC optimize("O3")
# pragma GCC optimize ("Ofast")
# pragma GCC optimize ("unroll-loops")
# pragma GCC target("sse,sse2,sse3,ssse3,sse4,avx,avx2")
using namespace std;
int sqrtn,res=0,l,r;
int ret[1231231],b[1234123],a[1231231];
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
		a[x]+=1;
		if (a[x]==1) res+=1;
	}
	else{
		a[x]-=1;
		if (a[x]==0) res-=1;
	}
}


int main(){
	cin.tie(0);cout.tie(0);
	ios::sync_with_stdio(false);
	int n;cin >> n;
	sqrtn=sqrt(n);
	vector<int> t;
	for (int i=1;i<=n;i++){
		cin >> b[i];
		t.push_back(b[i]);
	}
	sort(t.begin(),t.end());
	for (int i=1;i<=n;i++){
		b[i]=lower_bound(t.begin(),t.end(),b[i])-t.begin();
	}
	int m;cin >> m;
	for (int i=0;i<m;i++){
		tree.push_back({0,0,0});
		cin >> tree[i].l>>tree[i].r;
		tree[i].num=i;
	}
	sort(tree.begin(),tree.end());
	l=tree[0].l;
	r=tree[0].l-1;
	for (int i=0;i<m;i++){
		int xl=tree[i].l,xr=tree[i].r;
		while (xl<l) update(b[--l],1);
		while (l<xl) update(b[l++],-1);
		while (r<xr) update(b[++r],1);
		while (xr<r) update(b[r--],-1);
		ret[tree[i].num]=res;
	}
	for (int i=0;i<m;i++) cout << ret[i] << '\n';
}