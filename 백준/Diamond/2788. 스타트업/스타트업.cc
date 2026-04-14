#include<bits/stdc++.h>
using namespace std;
typedef long long ll;
const int MAX=2097153;
struct line{
	ll a,b;
	bool operator !=(const line & x){
		return a!=x.a || b!=x.b;
	}
};
struct Kinetic{
	ll n,T;
	vector<line> tree;
	vector<ll> melt;
	Kinetic(ll _n) : n(_n), T(0), tree(4*_n+1, {0, LLONG_MAX}), melt(4*_n+1, LLONG_MAX) {}
	ll f(const line& a,ll x){
		return a.a*x+a.b;
	}
	bool cmp(const line& line1,const line& line2){
		ll x=f(line1,T);
		ll y=f(line2,T);
		if (x!=y) return x<y;
		return line1.a<line2.a;
	}
	
	ll next(const line& line1,const line& line2){
		if (line1.a>line2.a){
			ll d=f(line2,T)-f(line1,T);
			ll ds=line1.a-line2.a;
			ll mint=T+(d-1)/ds+1;
			return mint>T ? mint : LLONG_MAX;
		}
		return LLONG_MAX;
	}
	
	void update1(ll n,ll st,ll ed){
		if (st==ed || melt[n]>T) return;
		
		ll m=(st+ed)/2;
		update1(n*2+1,st,m);
		update1(n*2+2,m+1,ed);
		
		auto line1=tree[2*n+1],line2=tree[2*n+2];
		if (!cmp(line1,line2)){
			swap(line1,line2);
		}
		tree[n]=line1;
		
		melt[n]=min(melt[2*n+1],melt[2*n+2]);
		if (line1!=line2){
			melt[n]=min(melt[n],next(line1,line2));
		}
	}
	void update(ll n,ll st,ll ed,int i,ll a,ll b){
		if (i<st || i>ed) return;
		if (st==ed){
			tree[n]={a,b};
			return;
		}
		ll m=(st+ed)/2;
		update(n*2+1,st,m,i,a,b);
		update(n*2+2,m+1,ed,i,a,b);
		melt[n]=0;
		update1(n,st,ed);
	}
	
	void update(int i,ll a,ll b){
		update(0,0,n-1,i,a,b);
	}

	void max_update(int i,ll a,ll b){
		update(0,0,n-1,i,-a,-b);
	}
	
	ll query(ll n,ll st,ll ed,ll l,ll r){
		if (ed<l || st>r)  return LLONG_MAX;
		update1(n, st, ed);
		if (l<=st && ed<=r) return f(tree[n],T);
		ll m=(st+ed)/2;
		return min(query(n*2+1,st,m,l,r),query(2*n+2,m+1,ed,l,r));
	}
	ll query(int s,int e){
		return query(0,0,n-1,s,e);
	}
	
	ll max_query(int s,int e){
		return -query(0,0,n-1,s,e);
	}
	void heaten(ll temp){
		T=temp;
		update1(0,0,n-1);
	}
};

int main(){
    cin.tie(0);cout.tie(0);
    ios::sync_with_stdio(false);
    int n,m;cin >> n >> m;
    Kinetic tree(1000000);
    while (m--){
    	int x;cin >> x;
    	if (x==1){
    		ll t,k,z,s;cin >>t >> k >> z >> s;
			tree.heaten(t);
			tree.max_update(k,z,s-t*z);	
		}
		else{
			ll t,a,b;cin >>t >> a >> b;
			if (a>b) swap(a, b);
			tree.heaten(t);
			ll v= tree.query(a,b);
			if (v==LLONG_MAX) cout << "nema\n";
			else cout << tree.max_query(a,b) << '\n';
		}
	}
}