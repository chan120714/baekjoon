#include<stdio.h>
#include<math.h>

long long tree[2097152];
long long a[1000001];
long long init(int node,int st,int ed){

	if (st==ed){
		return tree[node]=a[st];
	}
	else{
		return tree[node]=init(node*2,st,(st+ed)/2)+init(node*2+1,(st+ed)/2+1,ed);
	}
}
void update(int node,int st,int ed,int index,long long val){
	if (index<st || index>ed){
		return;
	}
	if (st==ed){
		tree[node]=val;
		a[st]=val;
		return;
	}
	else{
		update(node*2,st,(st+ed)/2,index,val);
		update(node*2+1,(st+ed)/2+1,ed,index,val);
		tree[node]=tree[node*2]+tree[node*2+1];
	}
}
long long query(int node,int st,int ed,int l,int r){
	long long lsum,rsum;
	if (st>r || ed<l){
		return 0;
	}
	if (l<=st && ed<=r){
		return tree[node];
	}
	lsum=query(node*2,st,(st+ed)/2,l,r);
	rsum=query(node*2+1,(st+ed)/2+1,ed,l,r);
	return lsum+rsum;
}
main(){
	int n,m,k,p,q;
	long long l,t;
	scanf("%d %d %d",&n,&m,&k);
	for (int i=0;i<n;i++){
		scanf("%lld",&l);
		a[i]=l;
	}
	init(1,0,n-1);
	for (int i=0;i<(m+k);i++){
		scanf("%d %d %lld",&q,&p,&t);
		if (q==1){
			update(1,0,n-1,p-1,t);
		}
		else{
			printf("%lld\n",query(1,0,n-1,p-1,t-1));
		}
	}
}