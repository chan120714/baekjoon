#include<bits/stdc++.h>
#pragma GCC optimized("Ofast")
using namespace std;
typedef long long ll;
struct Node{
	Node *l,*r;
	ll v;
	Node(){
		l=r=NULL;
		v=0;
	}
};
Node *tree[123456];
void init(Node *n,int s,int e){
	if (s==e){
		n->v=0;
		return;
	}
	n->l=new Node();
	n->r=new Node();
	int m=s+e>>1;
	init(n->l,s,m);init(n->r,m+1,e);
	n->v=n->l->v+n->r->v;
	return;
}
void update(Node *ptr,Node *n,int s,int e,int v,int idx){
	if (s==e){
		n->v+=v;
		return;
	}
	int mid=s+e>>1;
	if (mid<idx){
		n->l=ptr->l;
		n->r=new Node();
		update(ptr->r,n->r,mid+1,e,v,idx);
	}
	else{
		n->r=ptr->r;
		n->l=new Node();
		update(ptr->l,n->l,s,mid,v,idx);
	}
	n->v=n->l->v+n->r->v;
	return;
}
int query(Node*ptr,Node *n,int s,int e,int v){
	if (s==e) return s;
	int m=s+e>>1;
	int val=n->l->v-ptr->l->v;
	if (val<v){
		return query(ptr->r,n->r,m+1,e,v-val);
	}
	else{
		return query(ptr->l,n->l,s,m,v);
	}
}
vector<int> zip(vector<int> a){
	sort(a.begin(),a.end());
	return a;
}
int main(){
	cin.tie(0);cout.tie(0);
	ios::sync_with_stdio(false);
	for (int i=0;i<123456;i++) tree[i]=(Node *)malloc(sizeof(Node));
	int n,m;
	cin >> n >> m;
	init(tree[0],1,n);
	vector<int> a(n);
	for (int i=0;i<n;i++) cin >> a[i];
	vector<int> b=zip(a);
	for (int i=1;i<=n;i++){
		update(tree[i-1],tree[i],1,n,1,lower_bound(b.begin(),b.end(),a[i-1])-b.begin()+1);
	}
	while (m--){
		int x,y,z;
		cin >> x >> y >> z;
		cout << b[query(tree[x-1],tree[y],1,n,z)-1]<<'\n';
	}
	return 0;
}