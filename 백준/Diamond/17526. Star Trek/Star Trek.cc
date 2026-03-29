#include<bits/stdc++.h>
using namespace std;
typedef long long ll;
const ll INF=1e18l;

struct coor{ // ax+b
    ll a,b;
};

struct Node{
	coor line;
	Node *l, *r;
	Node(coor v) : line(v), l(nullptr), r(nullptr) {}
};

struct LiChao{
	ll s,e;
	Node *root;
	
	LiChao(ll _s, ll _e) : s(_s), e(_e), root(nullptr) {}
	 
    ll f(coor& a,ll x){
        return (a.a*x+a.b);
    }
    
    void add(coor cur,ll l,ll r,Node*& node){
    	if (!node){
    		node=new Node(cur);
    		return;
		}
		if (node->line.a == cur.a){
			if (node->line.b <= cur.b) return;
			node->line = cur;
			return;
		}
		
		ll m=l+(r-l)/2;
		
		bool lef = f(cur,l) < f(node->line,l);
		bool mid = f(cur,m) < f(node->line,m);
		
		if (mid) swap(node->line,cur);
		
		if (l==r) return;
		
		if (lef^mid) add(cur,l,m,node->l);
		else add(cur,m+1,r,node->r);
	}
    
    void add(ll a,ll b){
    	add({a,b},s,e,root);
	}
	
    ll query(ll x,ll l,ll r,Node* node){ // x에서의 최솟값 
        if (!node) return INF;
        
        ll res = f(node->line,x);
        if (l==r) return res;
        
        ll m=l+(r-l)/2;
        if (x<=m) return min(res,query(x,l,m,node->l));
        else return min(res,query(x,m+1,r,node->r));
    }
    
    ll query(ll x){
    	return query(x,s,e,root);
	}
	
    void add_max(ll m, ll b){
        add(-m, -b);
    }
    
    ll query_max(ll x){
        return -query(x);
    }
};

int main(){
	cin.tie(0);cout.tie(0);
	ios::sync_with_stdio(false);
	int n;cin >> n;
	LiChao lichao(-1000000000000ll,1000000000000ll);
	vector<ll> a(n);
	for (int i=1;i<n;i++) cin >> a[i];
	ll s=0;
	for (int i=0;i<n-1;i++){
		s+=a[i];
		ll x,y;cin >> x>> y;
		if (i==0){
			lichao.add(y,x);
			continue;
		}
		lichao.add(y,x+lichao.query(s)-y*s);
		
	}
	cout << lichao.query(s+a[n-1]);
}