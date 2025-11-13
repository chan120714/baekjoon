#include<bits/stdc++.h>
using namespace std;
typedef long long ll;
const ll MOD=786433;
const ll G=10;

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

vector<ll> ntt(vector<ll> a,ll R){
	int n=a.size();
	
    if (n==3){
        vector<ll> b(3);
        b[0]=a[0];
        b[1]=(a[0]+a[1]*R+a[2]*R%MOD*R)%MOD;R=R*R%MOD;
        b[2]=(a[0]+2*a[1]*R+a[2]*R*R)%MOD;
        return b;
    }
	vector<ll> A,B;
	for (int i=0;i<n;i++){
        if (i%2) B.push_back(a[i]);
        else A.push_back(a[i]);
    }
    
    A=ntt(A,R*R%MOD);
    B=ntt(B,R*R%MOD);
	
    ll w=1;
	for (int k=0;k<n/2;k++){
		ll u=A[k];
		ll v=B[k]*w%MOD;
				
		a[k]=(u+v)%MOD;
				
		a[k+n/2]=(u-v+MOD)%MOD;
				
		w*=R;
		w%=MOD;
	}
    return a;
}

int res[1230121];
int main(){
    cin.tie(0);cout.tie(0);
    ios::sync_with_stdio(false);
	vector<ll> a(786432);
    int n;cin >> n;
    for (int i=0;i<=n;i++){
        cin >> a[i];
    }
    
    auto c=ntt(a,G);
    
    res[0]=a[0];

    int t=1;
    for (int i=0;i<MOD-1;i++){
        res[t]=c[i];
        t*=G;
        t%=MOD;
    }
    int x;cin >> x;
    for (int i=0;i<x;i++){
        int x;cin >> x;
        cout << res[x] << '\n';
    }
}   