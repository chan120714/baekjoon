#include<bits/stdc++.h>
using namespace std;
typedef long long ll;
typedef pair<int,int> pi;
const ll MAX= 2147483647;
struct node{
	ll lmax,rmax,maxv,sumv;
};

struct pos{
	ll x,y,w;
	bool operator<(pos &a){
		if (y==a.y) return x<a.x;
		return y<a.y;
	}
};

vector<int> x,y;
vector<node> tree;
ll res=0;

node combine(node l,node r){
	node x;
	x.lmax=max(l.lmax,l.sumv+r.lmax);
	x.rmax=max(r.rmax,r.sumv+l.rmax);
	x.maxv=max(l.maxv,max(r.maxv,l.rmax+r.lmax));
	x.sumv=l.sumv+r.sumv;
	return x;
}

node update(int n,int s,int e,int a,ll val){
	if (a<s || e<a) return tree[n];
	if (s==e) return tree[n]={tree[n].maxv+val,tree[n].maxv+val,tree[n].maxv+val,tree[n].maxv+val};
	return tree[n]=combine(update(n*2,s,(s+e)/2,a,val),update(n*2+1,(s+e)/2+1,e,a,val));
}

node query(int n,int s,int e,int l,int r){
	if (e<l || r<s) return {-MAX,-MAX,-MAX,0};
	if (l<=s && e<=r) return tree[n];
	return combine(query(n*2,s,(s+e)/2,l,r),query(n*2+1,(s+e)/2+1,e,l,r));
}

int main(){
	cin.tie(0);cout.tie(0);
	ios::sync_with_stdio(false);
	int n; cin >> n;
	vector<pos> a(n);
	for (int i=0;i<n;i++){
		cin >> a[i].x >> a[i].y >> a[i].w;
		x.push_back(a[i].x);
		y.push_back(a[i].y);
	}
	x.push_back(-1);
	y.push_back(-1);
	sort(x.begin(),x.end());
	sort(y.begin(),y.end());
	sort(a.begin(),a.end());
	for (int i=1;i<=n;i++){
		if (y[i]==y[i-1]) continue;
		tree.clear();tree.resize(15000);
		int k=0;
		for (int j=i;j<=n;j++){
			if (y[j]==y[j-1]) continue;
			while (a[k].y<y[i]) k++;
			while (k<n && a[k].y<=y[j] && a[k].y>=y[i]){
				update(1,1,n,lower_bound(x.begin(),x.end(),a[k].x)-x.begin(),a[k].w);
				k++;
			}
			res=max(res,query(1,1,n,1,n).maxv);
		}
	}
	cout << res;
}