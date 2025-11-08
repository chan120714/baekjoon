#include<bits/stdc++.h>
using namespace std;
typedef long long ll;
const ll MOD=1000000007;
ll ipow(ll x,ll y){
    ll res=1;
    while (y){
        if (y&1){
            res*=x;
            res%=MOD;
        }
        x*=x;
        x%=MOD;
        y>>=1;
    }
    return res;
}
ll b[5254]={1,1,2,5,15,},f[12345]={1,};
int comb[5012][5012],parent[5412];
int find(int x){
    if (x==parent[x]) return x;
    else return parent[x]=find(parent[x]);
}

void unioned(int x,int y){
    x=find(x);
    y=find(y);

    if (x==y) return;
    if (x>y) swap(x,y);
    parent[y]=x;
}
int main(){
    cin.tie(0);cout.tie(0);
    ios::sync_with_stdio(false);
    for (int i=1;i<12345;i++) f[i]=f[i-1]*i%MOD;

    comb[0][0]=1;
    for (int i=1;i<=5000;i++){
        parent[i]=i;
        comb[i][0]=1;
        comb[i][i]=1;
        for (int j=1;j<i;j++){
            comb[i][j]=comb[i-1][j-1]+comb[i-1][j];
            comb[i][j]%=MOD;
        }
    }

    for (int i=5;i<=5000;i++){
        ll res=0;
        for (int j=0;j<i;j++){
            res+=comb[i-1][j]*b[j];
            res%=MOD;
        }
        b[i]=res;
    }
    
    int n,q;cin >> n >> q;

    while (q--){
        int x,y;cin >> x >> y;
        if (find(x)!=find(y)){
            unioned(x,y);
            n-=1;
        }
        cout << b[n]  <<'\n';
    }
    return 0;
}