#include<stdio.h>
#include<math.h>

long long tree[2097152],lazy[2097152];
long long a[1000001];
long long init(int node,int st,int ed){

	if (st==ed){
		return tree[node]=a[st];
	}
	else{
		return tree[node]=init(node*2,st,(st+ed)/2)+init(node*2+1,(st+ed)/2+1,ed);
	}
}
void update_lazy(int node,int st,int ed){
	if (lazy[node]!=0){
		tree[node]+=lazy[node]*(ed-st+1);
		if (st!=ed){
			lazy[node*2]+=lazy[node];
			lazy[node*2+1]+=lazy[node];
		}
		lazy[node]=0;
	}
}
void update_range(int node,int st,int ed,int l,int r,long long val){
	update_lazy(node,st,ed);
	if (r<st || l>ed){
		return;
	}
	if (l<=st && ed<=r){
		tree[node]+=val*(ed-st+1);
		if (st!=ed){
			lazy[node*2]+=val;
			lazy[node*2+1]+=val;
		}
		return;
	}
	else{
		update_range(node*2,st,(st+ed)/2,l,r,val);
		update_range(node*2+1,(st+ed)/2+1,ed,l,r,val);
		tree[node]=tree[node*2]+tree[node*2+1];
	}
}
long long query(int node,int st,int ed,int l,int r){
	long long lsum,rsum;
	update_lazy(node,st,ed);
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
	int n,m,k,p,q,w,e;
	long long l,t;
	scanf("%d %d %d",&n,&m,&k);
	for (int i=0;i<n;i++){
		scanf("%lld",&l);
		a[i]=l;
	}
	init(1,0,n-1);
	for (int i=0;i<(m+k);i++){
		scanf("%d",&q);
		if (q==1){
			scanf("%d %d %lld",&w,&e,&t);
			update_range(1,0,n-1,w-1,e-1,t);
		}
		else{
			scanf("%d %d",&w,&e);
			printf("%lld\n",query(1,0,n-1,w-1,e-1));
		}
	}
}