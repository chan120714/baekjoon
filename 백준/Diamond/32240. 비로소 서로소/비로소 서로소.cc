#include<bits/stdc++.h>
typedef long long ll;
#define MAX 30005000
using namespace std;
ll mobius[MAX];
unordered_map<ll,ll> mp;
const ll MOD=1000000007;
//mertens Trick
ll xudyh(ll n){
	__int128 i,j,r=1;
	if (n<MAX){
		return mobius[n];
	}
	if (mp.find(n)!=mp.end()){
		return mp[n];
	}
	for (i=2;i<=n;i=j+1){
		j=n/(n/i);
		r-=((((j-i+1)*(i+j)/2)%MOD)*xudyh(n/i))%MOD;
		r+=MOD;
		r%=MOD;
	}
	mp[n]=r;
	return r;
}


bool visited[MAX];
void init(){
	mobius[1]=1;
	vector<int> prime;
	for (int i=2;i<MAX;i++){
		if (visited[i]==0){
			prime.push_back(i);
			mobius[i]=-1;
		}
		if (1==1){
			for (auto j:prime){
				if (i*j>=MAX) break;
				visited[i*j]=1;
				if (i%j==0){
					mobius[i*j]=0;
					break;
				}
				else{
					mobius[i*j]=-mobius[i];
				}
			}
		}
	}
	for (int i=1;i<MAX;i++){
		mobius[i]=(mobius[i]*i)%MOD+mobius[i-1];
		mobius[i]+=MOD;mobius[i]%=MOD;
	}
}
int main(){
	ll a,st=-50000,ed=50000,x=1,y,val=0,mid,res;
	scanf("%lld",&a);
	init();
	for (ll i=1,j;i<=a;i=j+1){
		j=a/(a/i);
		ll t=xudyh(j)-xudyh(i-1),k=(a/i)%MOD;
		t+=MOD;t%=MOD;
		x=k*k;x%=MOD;
		x*=(k+1)%MOD;x%=MOD;
		val+=(x*t)%MOD;val%=MOD;
	}
	cout << val;
}