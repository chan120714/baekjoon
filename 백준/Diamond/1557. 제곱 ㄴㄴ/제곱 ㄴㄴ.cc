#include<bits/stdc++.h>
typedef long long ll;
using namespace std;
#define MAX 10010000
ll mobius[MAX]={0,1};
unordered_map<ll,ll> mp;
double pi=3.14159265358979323846;
//mertens Trick
ll xudyh(int n){
	ll i,j,r=1;
	if (n<MAX){
		return mobius[n];
	}
	if (mp.find(n)!=mp.end()){
		return mp[n];
	}
	for (i=2;i<=n;i=j+1){
		j=n/(n/i);
		r-=(j-i+1)* xudyh(n/i);
	}
	mp[n]=r;
	return r;
}

ll double_count(ll n){
	ll i,j,res=0;
	for (i=1;i*i<=n;i=j+1){
		j=sqrt(n/(n/(i*i)));
		res+=(n/(i*i))*(xudyh(j)-xudyh(i-1));
	}
	return res;
}
int main(){
	ll a,st=-5000,ed=5000,x,y,val,mid,res;
	scanf("%lld",&a);
	val=(ll)(a*pi*pi/(6));
	st+=val;
	ed+=val;
	st=max(st,0ll);
	ed=min(ed,3000000000000000000ll);
	for (int i=1;i<MAX;++i){
		for (int j=2;j*i<MAX;++j){
			mobius[i*j]-=mobius[i];
		}
		mobius[i]+=mobius[i-1];
	}
	while (st<=ed){
		mid=(st+ed)>>1;
		if (double_count(mid)>=a){
			ed=mid-1;
			res=mid;
		}
		else st=mid+1;
	}
	printf("%lld",res);
}
/*
1557B 맞추기
1557B 맞추기
1557B 맞추기
1557B 맞추기
1557B 맞추기
1557B 맞추기
1557B 맞추기
1557B 맞추기
1557B 맞추기
1557B 맞추기
1557B 맞추기
1557B 맞추기
1557B 맞추기
1557B 맞추기
1557B 맞추기
1557B 맞추기
1557B 맞추기
1557B 맞추기
1557B 맞추기
1557B 맞추기
1557B 맞추기
1557B 맞추기
1557B 맞추기
1557B 맞추기
1557B 맞추기
1557B 맞추기
1557B 맞추기
1557B 맞추기
1557B 맞추기
1557B 맞추기
1557B 맞추기
1557B 맞추기
1557B 맞추기
1557B 맞추기
1557B 맞추기
1557B 맞추기
1557B 맞추기
1557B 맞추기
1557B 맞추기
1557B 맞추기
1557B 맞추기
1557B 맞추기
1557B 맞추기 
1557B 맞추기 
1557B 맞추기 
1557B 맞추기 
 */