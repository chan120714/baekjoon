#include<bits/stdc++.h>
using namespace std;
typedef long long ll;
struct node{
	ll sum,mex;
}tree[4000004];
node merge(node x,node y){
	node a;
	a.mex=min(x.mex,y.mex);
	a.sum=x.sum+y.sum;
	return a;
}
void init(int n,int s,int e){
	if (s==e) {
		tree[n].mex=s;
		return;
	}
	init(n*2,s,(s+e)/2);
	init(n*2+1,(s+e)/2+1,e);
	tree[n]=merge(tree[n*2],tree[n*2+1]);
}


void update(int n,int s,int e,int v,int i){
	if (i<s || e<i )return;
	if (s==e) {
		tree[n].sum+=v;
		tree[n].mex+=v*998244353;
		return;
	}
	update(n*2,s,(s+e)/2,v,i);
	update(n*2+1,(s+e)/2+1,e,v,i);
	tree[n]=merge(tree[n*2],tree[n*2+1]);
	return;
}

int q(){
	return tree[1].mex;
}
int query(int n,int s,int e,int l,int r){
	if (e<l || r<s) return 0;
	if (l<=s && e<=r) return tree[n].sum;
	return query(n*2,s,(s+e)/2,l,r)+query(n*2+1,(s+e)/2+1,e,l,r);
}
int main(){
	cin.tie(0);cout.tie(0);
	ios::sync_with_stdio(false);
	int T;cin >> T;
	init(1,1,1000001);
	while (T--){
		int x,y; cin >> x >> y;
		if (x==1){
			update(1,1,1000001,1,y);
			cout << query(1,1,1000001,1,q()) << '\n';
		}
		else{
			update(1,1,1000001,-1,y);
			cout << query(1,1,1000001,1,q()) << '\n';
		}
	}
}