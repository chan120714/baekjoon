#include<bits/stdc++.h>
using namespace std;
//이거 오프라인 쿼리 붙어있겠네
//누적합 이용하는 방식을 O(n log n)으로 가능 할듯? 
struct node{
	node *l,*r;
	int v=0;
	node(){l=r=NULL;v=0;}
};
node *tree[12345];
void init(node *n,int s,int e){
	if (s==e) return;
	n->l=new node();
	n->r=new node();
	int m=(s+e)>>1;
	init(n->l,s,m);
	init(n->r,m+1,e);
	return;
}
void update(node *pre,node *n,int s,int e,int idx){
	if (s==e){
		n->v=pre->v+1;
		return;
	}
	int m=(s+e)>>1;
	if (idx<=m){
		n->r=pre->r;
		n->l=new node();
		update(pre->l,n->l,s,m,idx);
	}
	else{
		n->l=pre->l;
		n->r=new node();
		update(pre->r,n->r,m+1,e,idx);
	}
	n->v=n->l->v+n->r->v;
	return;
}

int query(node *st,node *ed,int s,int e,int l,int r){
	if (r<s || e<l) return 0;
	if (l<=s && e<= r) return ed->v-st->v;
	return query(st->l,ed->l,s,(s+e)/2,l,r)+query(st->r,ed->r,(s+e)/2+1,e,l,r);	
}

bool cmp(pair<int,int> x,pair<int,int> y){
	if (x.first==y.first) return x.second<y.second;
	return x.first<y.first;
}
int main(){
	cin.tie(0);cout.tie(0);
	ios::sync_with_stdio(false);
	int t;cin>>t;
	while (t--){
		int n,m,res=0; cin>>n>>m;
		vector<pair<int,int> > a(n);
		for (int i=0;i<12345;i++) tree[i]=new node();
		for (int i=0;i<n;i++) cin>>a[i].first>>a[i].second;
		sort(a.begin(),a.end(),cmp);
		a.push_back({120321,132341});
		init(tree[0],0,100000);
		for (int i=0;i<n;i++){
			update(tree[i],tree[i+1],0,100000,a[i].second);
		}
		while (m--){
			int x1,x2,y1,y2,t1,t2;
			cin >> x1 >>x2 >>y1 >>y2;
			pair<int,int> p1,p2;
			p1={x1-1,111111};p2={x2+1,-9};
			t1=lower_bound(a.begin(),a.end(),p1,cmp)-a.begin();
			t2=lower_bound(a.begin(),a.end(),p2,cmp)-a.begin();
			res+=query(tree[t1],tree[t2],0,100000,y1,y2);
		}
		cout << res<<'\n';
	}
}