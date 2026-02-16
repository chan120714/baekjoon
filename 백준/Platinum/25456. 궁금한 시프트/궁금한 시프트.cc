/*
virtual contest
그게왜진조잘못이느냐: kangsm02, Yoisaki-Kanade, saywoo
*/

#include <bits/stdc++.h>
using namespace std;

// NTT 템플릿 출처 : chan120714님 코드
using ll = long long int;
const ll MOD = 998244353;
const ll G = 3;

ll ipow(ll x, ll y) {
    ll res = 1;
    while (y) {
        if (y & 1) res = res * x % MOD;
        x = x * x % MOD;
        y >>= 1;
    }
    return res;
}

void ntt(vector<ll> &a, bool inv){
    int n = a.size();

    // bit reversal
    for (int i = 1, j = 0; i < n; i++){
        int b;
        for (b = n >> 1; j & b; b >>= 1) j ^= b;
        j ^= b;
        if (i < j) swap(a[i], a[j]);
    }
    
    for (int i = 2; i <= n; i <<= 1){
        ll wl = ipow(G, (MOD - 1) / i); //nth Roots of Unity
        if (inv) wl = ipow(wl, MOD - 2); // 역원
        
        for (int j = 0; j < n; j += i){
            ll w = 1;
            for (int k = 0; k < i / 2; k++){
                ll u = a[j+k], v = a[j+k+i/2] * w % MOD;
                a[j+k] = (u + v) % MOD;
                a[j+k+i/2] = (u - v + MOD) % MOD;
                w = w * wl % MOD;
            }
        }
    }
    // 역변환 
    if (inv) {
        ll ivn = ipow(n, MOD - 2);
        for (int i = 0; i < n; i++) a[i] = a[i] * ivn % MOD;
    }
}

vector<ll> mul(vector<ll> &A, vector<ll> &B){
	vector<ll> a=A,b=B;
    int n = 1;
    int x = a.size() + b.size() - 1;
    while (n < x) n <<= 1; // 2^n꼴로
    a.resize(n); b.resize(n); // 2^n 크기로 변환 

    ntt(a, 0); ntt(b, 0); // 정방향 변환
    for (int i = 0; i < n; i++) a[i] = a[i] * b[i] % MOD; // 곱셈 계산
    ntt(a, 1); // 역변환

    a.resize(x); // 필요한 크기로 변환
    return a;
}


int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    string S,T;
    cin >> S >> T;
    int n=S.size();
    
    vector<ll> a(2*n),b(n);
    
    for (int i=0;i<n;i++){
    	if (S[i]=='1'){
    		a[i]=1;
    		a[i+n]=1;
		}
	}
	
	for (int i=0;i<n;i++){
		if (T[i]=='1'){
			b[n-1-i]=1;
		}
	}
	vector<ll> c=mul(a,b);
	
	ll res=0;
	for (int i=0;i<n;i++){
		res=max(res,c[n-1+i]);
	}
	cout << res;
}