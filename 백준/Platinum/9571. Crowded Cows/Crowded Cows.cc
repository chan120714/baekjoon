#include<bits/stdc++.h>
using namespace std;
typedef long long ll;
const int MAX=1000000007;

struct A{
	A *l,*r;
	ll v;
	A(){
		l=r=NULL;
		v=0;
	}
};
A*saywoo;

void update(A *n,ll s,ll e,ll v,ll idx){
	if (s==e){
		n->v=max(n->v,v);
		return;
	}
	ll m=(s+e)>>1;
	if (!n->l) n->l = new A();
	if (!n->r) n->r = new A();
	if (idx<=m){
		update(n->l,s,m,v,idx);
	}
	else{
		update(n->r,m+1,e,v,idx);
	}
	ll x=n->r!=NULL ? n->r->v : 0;
	ll y=n->l!=NULL ? n->l->v : 0;
	n->v=max(x,y);
	return;
}

ll query1(A *n,ll s,ll e,ll l,ll r){
	if (!n) return 0;
	if (r<s || e<l) return 0;
	if (l<=s && e<=r) return n->v;
	ll m=s+e>>1;
	if (!n->l && !n->r) return 0;
	if (!n->l) return query1(n->r,m+1,e,l,r);
	if (!n->r) return query1(n->l,s,m,l,r);
	return max(query1(n->l,s,m,l,r),query1(n->r,m+1,e,l,r));
}

int main(){
	cin.tie(0);cout.tie(0);
	ios::sync_with_stdio(false);
	int n,d;cin >> n >> d;
	
	A k=A();
	vector<pair<int,int> > b;
	saywoo=&k;
	for (int i=1;i<=n;i++){
		ll x,y;cin >> x >> y;
		b.push_back({x,y});
		update(saywoo,1,MAX,y,x);
	}
	int res=0;
	for (auto i:b){
		if (query1(saywoo,1,MAX,max(1,i.first-d),i.first)>=i.second*2 && query1(saywoo,1,MAX,i.first,min(MAX,i.first+d))>=i.second*2){
			res+=1;
		}
	}
	cout << res;
}