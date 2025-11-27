#include<bits/stdc++.h>
using namespace std;
int d[123121];

void sol(){
    for (int i=0;i<102121;i++){
        d[i]=987654321;
    }
    int n;cin >> n;
    vector<pair<int,int> > a(n);
    int ret=0;
    for (int i=0;i<n;i++){
        cin >> a[i].first >> a[i].second;
        ret+=a[i].first;
    }

    d[ret]=0;
    for (auto j:a){
        for (int i=0;i<=100000;i++){
            d[i-j.first]=min(d[i-j.first],d[i]+j.second);
        }
    }
    int res=INT_MAX;
    for (int i=0;i<=100000;i++){
        res=min(res,max(d[i],i));
    }
    cout << res <<'\n';
}
int main(){
    cin.tie(0);cout.tie(0);
    ios::sync_with_stdio(false);
    int TC;cin >> TC;

    while (TC--){
        sol();
    }
}