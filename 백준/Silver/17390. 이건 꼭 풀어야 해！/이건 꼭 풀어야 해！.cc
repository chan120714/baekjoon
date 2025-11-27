#include<bits/stdc++.h>
using namespace std;
typedef long long ll;
typedef pair<int,int> pi;
typedef pair<ll,ll> pll;
int a[301231];
void u(int x,int v){while (x<=300000){a[x]+=v;x+=x&-x;}}
int q(int x,int res=0){while (x){res+=a[x];x-=x&-x;}return res;}
int query(int x,int y){
    return q(y)-q(x-1);
}
int main(){
    cin.tie(0);cout.tie(0);
    ios::sync_with_stdio(false);
    int n,q;cin >> n >> q;
    vector<int> a(n);

    for (int i=0;i<n;i++) cin >> a[i];
    sort(a.begin(),a.end());

    for (int i=0;i<n;i++) u(i+1,a[i]);

    while (q--){
        int x,y;cin >>x >> y;
        cout << query(x,y) << '\n';
    }
    return 0;
}