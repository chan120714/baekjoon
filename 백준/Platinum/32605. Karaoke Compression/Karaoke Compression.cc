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

int main(){
	cin.tie(0);cout.tie(0);
	ios::sync_with_stdio(false);
	Hash<12341,998244353> h1;
	Hash<98543,1234567891> h2;
	string a;cin >> a;
	h1.make(a);
	h2.make(a);
	
	int res,n;res=INT_MAX;n=a.size();
	for (int i=1;i<=n;i++){
		unordered_map<ll,int> t,te;
		vector<ll> p;
		for (int j=i;j<=n;j++){
			ll k=h1.get(j-i+1,j)*h2.get(j-i+1,j);
			res=min(res,i+n-(i-1)*(1+t[k]));
			p.push_back(k);
			if (j-i*2>=-1){
				if (j-te[p[j-i*2+1]]>=i){
					t[p[j-i*2+1]]+=1;
					te[p[j-i*2+1]]=j
				;}
			}
		}
	}
	cout << res;
}