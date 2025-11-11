#include<bits/stdc++.h>
using namespace std;
typedef long long ll;
int a[1021212],d[1021212];
int main(){
    cin.tie(0);cout.tie(0);
    ios::sync_with_stdio(false);
    int n,p;cin >> n >> p;p-=1;
    int res=0;
    for (int i=n;i>0;i--){
        int x;cin >> x;x%=p+1;
        d[i%p]+=x;
        d[i%p]%=p+1;
    }
    int x;cin >> x;
    p+=1;
    cout << x%p << '\n';
    
    d[0]+=x%p;
    d[0]%=p;

    for (int i=1;i<p;i++){
        res=0;
        int k=1;
        for (int j=0;j<p;j++){
            res+=d[j]*k%p;
            res%=p;
            k*=i;
            k%=p;
        }
        cout << res <<'\n';
    }
}