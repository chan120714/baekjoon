#include<bits/stdc++.h>
using namespace std;
typedef long long ll;
ll tree[1000000],a[1000000];
int n;
ll MOD=998244353;

void update(int x,int v){
    if (x==0) return;
    while(x<=n){
        tree[x]+=v;
        x+=x&-x;
    }
    return;
}

ll q(int x){
    ll res=0;
    while (x){
        res+=tree[x];
        x-=x&-x;
    }
    return res;
}

ll query(int x,int y){
    return q(y)-q(x-1);
}

ll res=0;

int main(){
    cin.tie(0);cout.tie(0);
    ios::sync_with_stdio(false);
    int q;cin >> n >> q;
    for (int i=1;i<=n;i++){
        cin >> a[i];
        update(a[i],1);
    }
    for (int i=2;i<=n;i++){
        ll t=query(i,n);
        res+=t*(t-1)/2*(i-1);
        res%=MOD;
    }
    while (q--){
        ll x,t;cin >> x >> t;
        if (t==1){
            update(a[x],-1);
            a[x]+=1;
            if (a[x]>1){
                t=query(a[x],n);
                res-=t*(t-1)/2*(a[x]-1)%MOD;
                update(a[x],1);
                t=query(a[x],n);
                res+=t*(t-1)/2*(a[x]-1);
                res+=MOD;
                res%=MOD;
            }
        }
        else{
            if (a[x]>1){
                t=query(a[x],n);
                res-=t*(t-1)/2*(a[x]-1)%MOD;
                res+=MOD;
                res%=MOD;
            }
            update(a[x],-1);
            if(a[x]>1){
                t=query(a[x],n);
                res+=t*(t-1)/2*(a[x]-1);
                res+=MOD;
                res%=MOD;
            }
            a[x]-=1;
            update(a[x],1);
        }
        cout << res <<'\n';
    }
}