#include<bits/stdc++.h>
#pragma GCC optimize("O3")
# pragma GCC optimize ("Ofast")
# pragma GCC optimize ("unroll-loops")
# pragma GCC target("sse,sse2,sse3,ssse3,sse4,avx,avx2")
using namespace std;
typedef long long ll;
int sqrtn;
int a[331231],arr[311232];
int cnt[332131],ret[323123],len[313212];
ll res=0,vv=0;

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
		if (cnt[x]>0) len[cnt[x]]-=1;
		cnt[x]+=1;
		len[cnt[x]]+=1;
		if (cnt[x]>res) res=cnt[x];
	}
	else{
		len[cnt[x]]-=1;
		cnt[x]-=1;
		if (cnt[x]>0) len[cnt[x]]+=1;
		if (len[res]==0) res-=1;
	}
	return;
}

int main(){
	cin.tie(0);cout.tie(0);
	ios::sync_with_stdio(false);
	int n,c; cin >> n >> c;
	sqrtn=sqrt(n);
	for (int i=1;i<=n;i++){
		cin >> arr[i];
	}
	int l,r;
	int m;cin >> m;
	for (int i=0;i<m;i++){
		tree.push_back({0,0,0});
		cin >> tree[i].l >> tree[i].r;
		tree[i].num=i;
	}
	sort(tree.begin(),tree.end());
	l=tree[0].l;
	r=tree[0].l-1;
	for (int i=0;i<m;i++){
		int xl=tree[i].l,xr=tree[i].r;
		while (r<xr) update(arr[++r],1);
		while (xl<l) update(arr[--l],1);
		while (xr<r) update(arr[r--],-1);
		while (l<xl) update(arr[l++],-1);
		if (res*2>(xr-xl+1)){
			for (int j=1;j<=c;j++){
				if (cnt[j]==res){
					ret[tree[i].num]=j;break;
				}
			}
		}
		else{
			ret[tree[i].num]=-1;
		}
	}
	for (int i=0;i<m;i++){
		if (ret[i]==-1){
			cout << "no\n";
		}
		else{
			cout << "yes "<<ret[i]<<'\n';
		}
	}
}