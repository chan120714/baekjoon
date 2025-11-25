#include<bits/stdc++.h>
using namespace std;
typedef long long ll;
typedef pair<int,int> pi;
typedef pair<ll,ll> pll;
#define x first
#define y second

int res1[312331],res2[312312];//1 -> minv / 2->maxv
int main(){
    cin.tie(0);cout.tie(0);
    ios::sync_with_stdio(false);
    int n,q;cin >> n >> q;
    vector<int> a(n);
    for (int i=0;i<n;i++) cin >> a[i];

    sort(a.begin(),a.end());

    
    for (int i=2;i<=300000;i++){
        int j=0;
        res1[i]=min(a[n-1]%i,a[0]%i);
        res2[i]=max(a[n-1]%i,a[0]%i);
        while (j<=300000){
            int t=lower_bound(a.begin(),a.end(),j)-a.begin();
            if (t!=0)res2[i]=max(res2[i],a[t-1]%i);
            if (t==n) break;
            res1[i]=min(res1[i],a[t]%i);
            j+=i;
        }
    }
    while (q--){
        int x;cin >> x;
        cout << res1[x] <<' '<<res2[x] << '\n'; 
    }
    return 0;
}