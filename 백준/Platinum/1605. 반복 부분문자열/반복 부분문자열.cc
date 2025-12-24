#include<bits/stdc++.h>
using namespace std;

using ll = long long int;

template<ll P, ll M> struct Hash {
    vector<ll> hash, p;
    void make(const string& s) {
        int len = s.length();
        hash.resize(len + 1); p.resize(len + 1);
        
        for (int i = 1; i <= len; i++) hash[i] = (hash[i-1] * P + s[i-1]) % M;
        p[0] = 1;
        for (int i = 1; i <= len; i++) p[i] = (p[i-1] * P) % M;
    }
    ll get(int l, int r) {
        ll h = (hash[r] - hash[l-1] * p[r-l+1]) % M;
        return h >= 0 ? h : h + M;
    }
};

//template by Saywoo


int main(){
	Hash<52299, 998244353> h1;
    Hash<129914, 1234567891> h2;
	int n;cin >> n;
	string a;cin >> a;
	h1.make(a);
    h2.make(a);
	int st=1,ed=n;
	int res=0;
	
	while (st<=ed){
		int mid=st+ed>>1;
		
		unordered_set<ll> b;
		int ist=0;
		for (int i=mid;i<=n;i++){
			ll x=h1.get(i-mid+1,i);
			ll y=h2.get(i-mid+1,i);
            
			if (b.find(x*y)!=b.end()){
				ist=1;
			}
			b.insert(x*y);
		}
		if (ist==0){
			ed=mid-1;
		}
		else{
			res=mid;
			st=mid+1;
		}
	}
	cout << res;
}