#include<bits/stdc++.h>
using namespace std;
typedef long long ll;
ll res[54321];
struct node{
	int parent;
	unordered_map<int,int> ret;
}tree[123543];

struct dd{
	int x,y,a;
	bool operator<(const dd &t)const{
		return a>t.a;
	}
};
int ist[112342];

int find(int n){
	if (tree[n].parent==n) return n;
	else return tree[n].parent=find(tree[n].parent);
}


void unioned(int x,int y,ll val){
	x=find(x);
	y=find(y);
	if (x==y) return;
	if (tree[x].ret.size()<tree[y].ret.size()){
		for (auto i:tree[x].ret){
			res[i.first]+=tree[y].ret[i.first]*i.second*val;
			tree[y].ret[i.first]=tree[y].ret[i.first]+i.second;
		}
	}
	else{
		swap(x,y);
		for (auto i:tree[x].ret){
			res[i.first]+=tree[y].ret[i.first]*i.second*val;
			tree[y].ret[i.first]=tree[y].ret[i.first]+i.second;
		}
	}
	tree[x].ret.clear();
	tree[x].parent=y;
}
int main(){
	cin.tie(0);cout.tie(0);
	int n,k,m;
	cin >> n >> k >> m;
	for (int i=1;i<=n;i++){int x;cin >> x;tree[i].ret[x]=1;tree[i].parent=i;}
	vector<dd> graph;
	while (m--){
		int a,b,c;
		cin >> a>> b>> c;
		graph.push_back({a,b,c});
	}
	sort(graph.begin(),graph.end());
	for (auto i:graph){
		unioned(i.x,i.y,i.a);
	}
	for (int i=1;i<=k;i++) cout << res[i] << '\n';
}