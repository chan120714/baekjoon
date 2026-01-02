#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
typedef pair<int,int> pi;
typedef pair<ll,ll> pll;


void solve(){
    ll n,d,m;cin >> n >> d >> m;
    vector<ll> a(n);
    for (int i=0;i<n;i++) cin >> a[i];

    sort(a.begin(),a.end());

    m*=d;
    ll res=0,cur=0,v=0;
    for (auto i:a){
        res+=max(0ll,d-cur);
        cur+=i;
        v+=1;
        if (res>=m)break;
    }
    if (res<m){
        cout << -1;
    }
    else{
        cout << v;
    }
}
int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    ll tc = 1;
    // cin >> tc;
    
    while(tc--) {
        solve();
    }
    
    return 0;
}