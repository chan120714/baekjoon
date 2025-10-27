#include<bits/stdc++.h>
using namespace std;
typedef long long ll;
const ll MAX=1000000000007;
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
	int n;cin >> n;
	A k=A();
	vector<pair<ll,ll>> a(n);
	
	for (int i=0;i<n;i++) cin >> a[i].first >> a[i].second;
	
	saywoo=&k;
	sort(a.begin(),a.end());
	a.erase(unique(a.begin(),a.end()), a.end());
	reverse(a.begin(),a.end());
	
	for (int i=0;i<a.size();i++){
		//cout << a[i].first <<' '<< a[i].second <<'\n';
		ll x=a[i].second;
		update(saywoo,0,MAX,query1(saywoo,0,MAX,0,x)+x,x);
	}
	cout << query1(saywoo,0,MAX,0,MAX);
}