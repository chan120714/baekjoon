#include<bits/stdc++.h>
using namespace std;
typedef long long ll;
typedef pair<int,int> pi;
typedef pair<ll,ll> pll;
int main(){
    cin.tie(0);cout.tie(0);
    ios::sync_with_stdio(false);
    int n,x,y;cin >> n;
    vector<pair<int,int> > a(n);
    for (int i=0;i<n;i++) cin >> a[i].first >> a[i].second;
    cin >> x >> y;

    int px=1,py=1,mx=1,my=1;
    for (auto i:a){
        int x1,y1;x1=i.first;y1=i.second;
        if (y1<y){
            if (y-y1>=abs(x-x1)){
                py=0;
            }
        }
        if (y1>y){
            if (y1-y>=abs(x-x1)){
                my=0;
            }
        }
        if (x1<x){
            if (x-x1>=abs(y-y1)){
                px=0;
            }
        }
        if (x1>x){
            if (x1-x>=abs(y-y1)){
                mx=0;
            }
        }
    }
    int res=mx+my+px+py;
    cout << (res>0 ? "YES" : "NO") ;
    return 0;
}