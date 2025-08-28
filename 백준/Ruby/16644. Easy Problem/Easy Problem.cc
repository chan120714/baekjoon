#include<bits/stdc++.h>
typedef long long ll;
#define MAX 30005000
using namespace std;
int mobius[MAX];
unordered_map<ll,ll> mp;
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
	ll i,j,res=n;
	for (i=2;i*i<=n;i=j+1){
		j=sqrt(n/(n/(i*i)));
		res+=(n/(i*i))*(xudyh(j)-xudyh(i-1));
	}
	return res;
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
					mobius[i*j]=mobius[i]*mobius[j];
				}
			}
		}
	}
	for (int i=2;i<MAX;i++){
		mobius[i]+=mobius[i-1];
	}
}
int main(){
	ll a,st=-50000,ed=50000,x,y,val,mid,res;
	scanf("%lld",&a);
	val=(ll)(a*1.6449340668482264060656916626612655818462371826171875);
	st+=val;
	ed+=val;
	if (a>1000000000000000ll){
		st+=10000;
		ed-=10000;
	}
	st=max(st,0ll);
	ed=min(ed,4000000000000000000ll);
	init();
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