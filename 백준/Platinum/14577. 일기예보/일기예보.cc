#include<bits/stdc++.h>
typedef long long ll;
using namespace std;
const ll MAX=100000000000000;
struct Node{
	Node *l,*r;
	int v;
	Node(){
		l=r=NULL;
		v=0;
	}
};
Node *tree;
void update(Node *n,ll s,ll e,int v,ll idx){
	if (s==e){
		n->v+=v;
		return;
	}
	ll m=(s+e)>>1;
	if (idx<=m){
	    if (!n->l) n->l = new Node();
		update(n->l,s,m,v,idx);
	}
	else{
        if (!n->r) n->r = new Node();
		update(n->r,m+1,e,v,idx);
	}
	ll x=n->r!=NULL ? n->r->v : 0;
	ll y=n->l!=NULL ? n->l->v : 0;
	n->v=x+y;
	return;
}
ll query1(Node *n,ll s,ll e,ll l,ll r){
	if (!n) return 0;
	if (r<s || e<l) return 0;
	if (l<=s && e<=r) return n->v;
	ll m=s+e>>1;
	if (!n->l && !n->r) return 0;
	if (!n->l) return query1(n->r,m+1,e,l,r);
	if (!n->r) return query1(n->l,s,m,l,r);
	return query1(n->l,s,m,l,r)+query1(n->r,m+1,e,l,r);
}
ll query2(Node *n,ll s,ll e,ll v){
	if (s==e) return s;
	ll m=s+e>>1;
    ll lv=(n->l ? n->l->v :0);
	if (v<=lv)return query2(n->l,s,m,v);
	else return query2(n->r,m+1,e,v-lv);
}
int main(){
	cin.tie(0);cout.tie(0);
	ios::sync_with_stdio(false);
	int n,m;
	cin >> n >> m;
	vector<ll> a(1+n);
	Node k=Node();
	tree=&k;
	for (int i=1;i<=n;i++){
		cin >> a[i];
		update(tree,0,MAX,1,a[i]);
	}
	for (int i=0;i<m;i++){
		ll x,y,z;
		cin >>x >> y;
		if (x==1){
			cin >>z;
			update(tree,0,MAX,-1,a[y]);
			a[y]+=z;
			update(tree,0,MAX,1,a[y]);
		}
		else if (x==2){
			cin >> z;
			update(tree,0,MAX,-1,a[y]);
			a[y]-=z;
			update(tree,0,MAX,1,a[y]);
		}
		else if (x==3){
			cin >> z;
            z=min(z,MAX);
			cout << query1(tree,0,MAX,y,z)<<'\n';
		}
		else{
			cout << query2(tree,0,MAX,n-y+1)<<'\n';
		}
	}
}