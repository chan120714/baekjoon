#include<bits/stdc++.h>
using namespace std;
typedef long long ll;
const ll MAX=1000000000000000123;

const int SMAX=201231;
int tree[SMAX*4];
void update(int n,int s,int e,int v,int idx){
    if (idx<s || e<idx) return;
    if (s==e){
        tree[n]+=v;
        return;
    }
    update(n*2,s,(s+e)/2,v,idx);
    update(n*2+1,(s+e)/2+1,e,v,idx);
    tree[n]=tree[n*2]+tree[n*2+1];
    return;
}

int query(int n,int s,int e,int l,int r){
    if (s>r || e<l) return 0;
    if (l<=s && e<=r) return tree[n];
    return query(n*2,s,(s+e)/2,l,r)+query(n*2+1,(s+e)/2+1,e,l,r);
}

ll ceildiv(ll p,ll q){
	if (q<0){
		p=-p;
		q=-q;
	}
	return (p>=0) ? (p+q-1)/q : p/q;
}

struct node{
	int type;
	ll a,b;
}s[231231];


int main(){
	cin.tie(0);cout.tie(0);
	ios::sync_with_stdio(false);
	unordered_map<ll, int> tt;
	int n,div0=0,si=0;cin >> n;
	vector<ll> t;
	t.push_back(-MAX-123);
	for (int i=0;i<n;i++){
		int a;cin >> a;
		if (a==1){
			ll b,c;cin >> b >> c;
			s[i]={a,b,c};
			t.push_back(ceildiv(-b,a));
		}
		else{
			ll b;cin >> b;
			s[i]={a,b,0};
			t.push_back(b);
		}
	}
	sort(t.begin(),t.end());
	t.erase(unique(t.begin(),t.end()),t.end());
    auto idx = [&](ll v){return int(lower_bound(t.begin(),t.end(), v)-t.begin())+1;};
	for (auto i:s){
		if (i.type==1){
			if (i.a==0){
				if (i.b<0) si^=1;
				if (i.b==0) div0=1;
				continue;
			}
			ll x=ceildiv(-i.b,i.a);
			if (i.b%i.a==0){
				tt[-i.b/i.a]=tt[-i.b/i.a]+1;
			}
			if (i.a<0){
				update(1,1,SMAX,1,idx(x));
				si^=1;
			}
			else{
				update(1,1,SMAX,1,1);
				update(1,1,SMAX,1,idx(x));
			}
		}
		else if (i.type==2){
			ll x=query(1,1,SMAX,idx(i.a)+1,SMAX);
			if (tt[i.a] || div0) cout << 0 << '\n';
			else if (si^(x&1)) cout << '-' << '\n';
			else cout << '+' << '\n';
		}
	}
}