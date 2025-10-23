#include<bits/stdc++.h>
using namespace std;

int a[1203201];
struct node{
	int max,min;
}tree[4010232];

node merge(node x,node y){
	return {max(x.max,y.max),min(x.min,y.min)};
}
node init(int n,int s,int e){
	if (s==e) return tree[n]={a[s],a[s]};
	return tree[n]=merge(init(n*2,s,(s+e)/2),init(n*2+1,(s+e)/2+1,e));
}

int max_query(int n,int s,int e,int l,int r){
	if (r<s || e<l) return INT_MIN;
	if (l<=s && e<=r) return tree[n].max;
	return max(max_query(n*2,s,(s+e)/2,l,r),max_query(n*2+1,(s+e)/2+1,e,l,r));
}
int min_query(int n,int s,int e,int l,int r){
	if (r<s || e<l) return INT_MAX;
	if (l<=s && e<=r) return tree[n].min;
	return min(min_query(n*2,s,(s+e)/2,l,r),min_query(n*2+1,(s+e)/2+1,e,l,r));
}
int q(int n,int s,int e){
	return max_query(1,1,n,s,e)-min_query(1,1,n,s,e);
}
int main(){
	cin.tie(0);cout.tie(0);
	ios::sync_with_stdio(false);
	int n,m,c;cin >> n >> m >> c;
	for (int i=1;i<=n;i++) cin >> a[i];
	init(1,1,n);
	int ist=0;
	for (int i=1;i<=n-m+1;i++){
		int s=q(n,i,i+m-1);
		if (s<=c){
			cout << i << ' ';
			ist =1;
		}
	}
	if (!ist){
		cout << "NONE";
	}
}