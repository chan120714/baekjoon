#include<iostream>
using namespace std;
typedef long long ll;
const ll mod=998244353;
ll ipow(ll x, ll p){
	ll ret = 1, piv = x;
	while(p){
		if(p & 1) ret = ret * piv % mod;
		piv = piv * piv % mod;
		p >>= 1;
	}
	return ret;
}
int main(){
    ll n;
    cin>>n;
    if (n==1){
    	cout << 1;
    	return 0;
	}
    ll ret=9676800,k=6,v=0;
    if (n<14){
        cout<<-1;
        return 0;
    }
    n-=12;
    while (n>=k*2){
        n-=k*2;
        k+=2;
        v++;
    }
    ll st=1,ed=12;
    while (v>0){
    	ll p=1;
        for (int i=st;i<=ed;i++){
			p*=i;
            p%=mod;
        }
        p=ipow(p,v);
        ret*=p;
        ret%=mod;
        st=ed+1;ed+=4;
        v-=1;
    }
    if (n>=k){
        n-=k;
        for (int i=1;i<=2*k-1;i+=2){
            ret*=i;
            ret%=mod;
        }
        for (int i=2;i<=2*n;i+=2){
            ret*=i;
            ret%=mod;
        }
    }
    else{
        for (int i=1;i<=2*n-1;i+=2){
            ret*=i;
            ret%=mod;
        }
    }
    cout <<ret;
}
