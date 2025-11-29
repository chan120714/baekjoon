#include<bits/stdc++.h>
using namespace std;
typedef long long ll;
typedef pair<int,int> pi;
typedef pair<ll,ll> pll;
#define x first
#define y second
int ist[201231];
int main(){
    cin.tie(0);cout.tie(0);
    ios::sync_with_stdio(false);
    ll n,k;cin >> n >> k;

    if (2*n-1>k) cout<<"impossible";
    else if(n*n<k) cout<<"impossible";
    else if(n*n-2==k) cout << "impossible";
    else{
        vector<int> a;
        ll t=k,st=1,v=0,i;
        if (t-(2*n-1)!=2 && t-(2*n-1)>=0){
            ist[n]=1;
            t-=(2*n-1);
        }
        else{
            t-=1;
            a.push_back(n);
        }
        for (int i=n-1;i>=1;i--){
            if (t-(2*i-1)!=2 && t-(2*i-1)>=0){
                ist[i]=1;
                t-=(2*i-1);
            }
        }
        for (int i=1;i<=n;i++){
            if (ist[i]==1){
                a.push_back(i);
            }
        }
        for (int i=n-1;i>=1;i--){
            if (ist[i]==0) a.push_back(i);
        }
        if (t){
            cout<<"impossible";
            return 0;
        }
        for (auto i:a){
            cout << 2*i-1 <<' ';
        }
    }
    return 0;
}