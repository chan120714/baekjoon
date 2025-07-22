#include<bits/stdc++.h>
using namespace std;
typedef long long ll;
typedef pair<ll,ll> pll;
typedef pair<int,int> pi;
struct node{
	int x,y,z;
	bool operator<(node &t){
		return x<t.x;
	}
};
vector<node> a;
int tree[2400000];
int update(int n,int s,int e,int v,int t){
	if (v<s || e<v) return tree[n];
	if (s==e) return tree[n]=t;
	return tree[n]=min(update(n*2,s,(s+e)/2,v,t),update(n*2+1,(s+e)/2+1,e,v,t));
}
int query(int n,int s,int e,int l,int r){
	if (r<s || e<l) return 1054651;
	if (l<=s && e<=r) return tree[n];
	return min(query(n*2,s,(s+e)/2,l,r),query(n*2+1,(s+e)/2+1,e,l,r));
}
int main(){
	cin.tie(0);cout.tie(0);
	ios::sync_with_stdio(false);
	int n,res=0;cin >> n;
	a.resize(n);
	for (int i=0;i<n;i++){
		int x;cin>>x;
		a[x-1].x=i+1;
	}
	for (int i=0;i<n;i++){
		int x;cin>>x;
		a[x-1].y=i+1;
	}
	for (int i=0;i<n;i++){
		int x;cin>>x;
		a[x-1].z=i+1;
	}
	for (int i=0;i<2400000;i++) tree[i]=1054651;
	sort(a.begin(),a.end());
	for (auto i:a){
		if (query(1,1,n,1,i.y)>i.z){
			res++;
		}
		update(1,1,n,i.y,i.z);
	}
	cout << res;
}