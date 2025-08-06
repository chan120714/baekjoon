#include<bits/stdc++.h>
using namespace std;
long long a[500002],tree[1000000];
long long dp[530000];
int init (int n,int s,int e){
	if (s==e){
		return tree[n]=a[s];
	}
	return tree[n]=min(init(n*2,s,(s+e)/2),init(n*2+1,(s+e)/2+1,e));
}
long long query(int n,int s,int e,int l,int r){
	if (s>r || e<l) return 2147483647;
	if (l<=s && e<=r) return tree[n];
	return min(query(n*2,s,(s+e)/2,l,r),query(n*2+1,(s+e)/2+1,e,l,r));
}
int main(){
	int n;
	long long res=0;
	cin >> n;
	for (int i=1;i<=n;i++) cin >> a[i];
	init(1,1,n);
	for (int i=1;i<=n;i++){
		dp[i]=dp[i-1]+a[i];
	}
	int r=1,l=1;
	for (int i=1;i<=n;i++){
		int left=i,st=1,ed=i;
		while (st<=ed){
			int mid = st + ed >> 1;
			if (query(1,1,n,mid,i)==a[i]){
				ed=mid-1;
				left=min(left,mid);
			}
			else st=mid+1;
		}
		if (a[st+ed>>1]>=a[i]) left=min(left,st+ed >>1);
		int right=i;
		st=i;ed=n;
		while (st<=ed){
			int mid = st + ed >> 1;
			if (query(1,1,n,i,mid)==a[i]){
				st=mid+1;
				right=max(mid,right);
			}
			else ed=mid-1;
		}
		if (a[st+ed>>1]>=a[i]) right=max(right,st+ed >>1);
		if (res<1ll*a[i]*(dp[right]-dp[left-1])){
			r=right;
			l=left;
			res=1ll*a[i]*(dp[right]-dp[left-1]);
		}
		
	}
	cout << res<<'\n'<<l<<' ' << r;
}