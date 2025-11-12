#include<bits/stdc++.h>
using namespace std;
typedef long long ll;
const ll MOD=998244353;
const ll G=3;

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

vector<ll> ntt(vector<ll> a,bool inv){
	int n=a.size();
	
	// bit reversal
	for (int i=1,j=0;i<n;i++){
		int b=n>>1;
		for (;j&b;b>>=1){
			j^=b;
		}
		j^=b;
		if (i<j) swap(a[i],a[j]);
	}
	
	for (int i=2;i<=n;i<<=1){
		//nth Roots of Unity
		ll wl=ipow(G,(MOD-1)/i);
		
		if (inv){
			// 역원 
			wl=ipow(wl,MOD-2);
		}
		
		for (int j=0;j<n;j+=i){
			ll w=1;
			for (int k=0;k<i/2;k++){
				ll u=a[j+k];
				ll v=a[j+k+i/2]*w%MOD;
				
				a[j+k]=(u+v)%MOD;
				
				a[j+k+i/2]=(u-v+MOD)%MOD;
				
				w*=wl;
				w%=MOD;
			}
		}
	}
	
	
	// 역변환 
	if (inv){
		ll ivn=ipow(n,MOD-2);
		for (int i=0;i<n;i++){
			a[i]*=ivn;
			a[i]%=MOD;
		}
	}
	return a;
}

vector<ll> mul(vector<ll> a,vector<ll> b){
	int n=1;
	int x=a.size()+b.size()-1;
	while (n<x) n*=2; // 2^n꼴로 
	 
	// 2^n 크기로 변환 
	a.resize(n);
	b.resize(n);
	
	// 정방향 변환
	a=ntt(a,0);
	b=ntt(b,0);
	
	
	for (int i=0;i<n;i++){
		a[i]*=b[i];
		a[i]%=MOD; // 곱셈 계산 
	}
	
	a=ntt(a,1);// 역변환 
	
	a.resize(x); // 필요한 크기로 변환
	 
	return a;
}

int t[1021021];
vector<ll> era(int x){
	vector<ll> ret;
	for (int i=0;i<1011021;i++){
		t[i]=1;
	}
	for (int i=2;i<=1000;i++){
		if (t[i]==1){
			int j=2;
			while (i*j<=x){
				t[i*j]=0;
				j+=1;
			}
		}
	}
    ret.push_back(0);
    ret.push_back(0);
	for (int i=2;i<=x;i++){
		if (t[i]) ret.push_back(1);
        else ret.push_back(0);
	}
	return ret;
}

int res[1230121];
int main(){
    cin.tie(0);cout.tie(0);
    ios::sync_with_stdio(false);
	auto a=era(1000001);
    vector<ll> b(1000001);

    for (int i=2;i<=500000;i++){
        if (a[i]){
            b[i*2]=1;
        }
    }
	auto c=mul(a,b);

	int T;cin >> T;
	while (T--){
		int x;cin >> x;
		cout << c[x] << '\n';
	}
}