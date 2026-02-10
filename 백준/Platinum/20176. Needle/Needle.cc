/*
virtual contest
그게왜진조잘못이느냐: kangsm02, Yoisaki-Kanade, saywoo
*/

#include <bits/stdc++.h>
using namespace std;

// NTT 템플릿 출처 : chan120714님 코드
using ll = long long int;
ll MOD = 998244353;
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

vector<ll> ntt(vector<ll> a, bool inv){
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
    return a;
}

vector<ll> mul(vector<ll> a, vector<ll> b){
    int n = 1;
    int x = a.size() + b.size() - 1;
    while (n < x) n <<= 1; // 2^n꼴로
    a.resize(n); b.resize(n); // 2^n 크기로 변환 

    a = ntt(a, 0); b = ntt(b, 0); // 정방향 변환
    for (int i = 0; i < n; i++) a[i] = a[i] * b[i] % MOD; // 곱셈 계산
    a = ntt(a, 1); // 역변환

    a.resize(x); // 필요한 크기로 변환
    return a;
}


int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    int u,m,l;
    cin >> u;
    vector<ll> a(100000),b(200000),c(100000);
    for (int i=0;i<u;i++){
        int x;cin >> x;
        a[x+30000]+=1;
    }
    cin >> m;
    for (int i=0;i<m;i++){
        int x;cin >> x;
        b[x*2+60000]+=1;
    }
    cin >> l;
    for (int i=0;i<l;i++){
        int x;cin >> x;
        c[x+30000]+=1;
    }
    
    vector<ll> d=mul(a,c);
    MOD=1004535809;
    vector<ll> e=mul(a,c);
    ll res=0;

    for (int i=0;i<d.size();i++){
        ll x=d[i],y=e[i];
        x=(x+1ll*998244353*(ipow(1ll*998244353,MOD-2)*((y-x+MOD)%MOD)%MOD))%(MOD*998244353);
        res+=x*b[i];
    }

    cout << res;
    return 0;
}