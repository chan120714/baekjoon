#include<bits/stdc++.h>
using namespace std;
const int MAX=32145;
struct offline{
	int type,a,b;
};

int parent[MAX],arr[MAX],tree[MAX*4];
int sz[MAX],dep[MAX],par[MAX],top[MAX],in[MAX],out[MAX];
vector<int> g[MAX];
int find(int n){
	if (n==parent[n]) return n;
	else return parent[n]=find(parent[n]);
}

void merge(int n,int m){
	int a=find(n),b=find(m);
	if (a<b){
		parent[b]=a;
	}
	else parent[a]=b;
}

bool visited[MAX],visited1[MAX];
void dfs1(int v,int last){
	if (visited[v]) return;
	sz[v]=1;
	visited[v]=true;
	for (auto &i:g[v]){
		if (i==last) continue;
		dep[i]=dep[v]+1;par[i]=v;
		dfs1(i,v);sz[v]+=sz[i];
		if (sz[i]>sz[g[v][0]]) swap(i,g[v][0]);
	}
}

int pv=0;
void dfs2(int v,int last,int n){
	if (visited1[v]) return;
	visited1[v]=true;
	in[v]=++pv;
	for (auto i:g[v]){
		if (i==last) continue;
		if (g[v][0]==i){
			top[i]=top[v];
		}
		else{
			top[i]=i;
		}
		dfs2(i,v,n);
	}
	out[v]=pv;
}

int init(int n,int s,int e){
	if (s==e){
		cout << s <<' '<< arr[in[s]];
		return tree[n]=arr[in[s]];
	} 
	else return tree[n]=init(n*2,s,(s+e)/2)+init(n*2+1,(s+e)/2+1,e);
}

void update(int n,int s,int e,int idx,int val){
	if (idx<s || e<idx) return;
	if (s==e){
		tree[n]=val;
		return;
	}
	update(n*2,s,(s+e)/2,idx,val);
	update(n*2+1,(s+e)/2+1,e,idx,val);
	tree[n]=tree[n*2]+tree[n*2+1];
	return;
}

int query(int n,int s,int e,int l,int r){
	if (r<s || e<l) return 0;
	if (l<=s && e<=r) return tree[n];
	return query(n*2,s,(s+e)/2,l,r)+query(n*2+1,(s+e)/2+1,e,l,r);
}

vector<offline> que;
int main(){
	cin.tie(0);cout.tie(0);
	ios::sync_with_stdio(false);
	for (int i=0;i<32145;i++) parent[i]=i;
	int n,T;cin >>n;
	for (int i=1;i<=n;i++) cin >> arr[i];
	cin >> T;
	for (int i=0;i<T;i++){
		string q;int w,e;
		cin >> q >> w >> e;
		if (q[0]=='e'){
			if (find(w)!=find(e)){
				que.push_back({-1,0,0}); // -1 -> impossible
			}
			else{
				que.push_back({1,w,e});
			}
		}
		else if (q[0]=='b'){
			if (find(w)==find(e)){
				que.push_back({-2,0,0}); // -2 -> no
			}
			else{
				merge(w,e);
				g[w].push_back(e);
				g[e].push_back(w);
				que.push_back({2,w,e}); // 2 -> yes
			}
		}
		else{
			que.push_back({0,w,e});
		}
	}
	for (int i=1;i<=n;i++) dfs1(i,-1);
	for (int i=1;i<=n;i++) dfs2(i,-1,n);
	/*
	init(1,1,n);
	for (int i=1;i<=n;i++) cout << in[i] << ' ';
	cout<<endl; 
	for (int i=1;i<=n;i++) cout << top[i] << ' ';
	cout<<endl; 
	for (int i=1;i<=n;i++) cout << par[i] << ' ';
	cout<<endl; 
	for (int i=1;i<=n;i++) cout << dep[i] << ' ';
	cout<<endl; */
	for (int i=1;i<=n;i++) update(1,1,n,in[i],arr[i]);
	for (auto i:que){
		if (i.type==-1) cout << "impossible\n";
		else if (i.type==-2) cout << "no\n";
		else if (i.type==2) cout << "yes\n";
		else if (i.type==1){
			int t1=i.a,t2=i.b,res=0;
			//cout << t1 <<' ' << t2 <<' ';
			while (top[t1]!=top[t2]){
				if (dep[top[t1]]<dep[top[t2]]) swap(t1,t2);
				//cout << t1 <<' ' << t2 << 'q';
				res+=query(1,1,n,in[top[t1]],in[t1]);
				//cout << query(1,1,n,in[top[t1]],in[t1]) <<'p';
				t1=par[top[t1]];
				//cout << t1 <<' ' << t2 << 'q';
			}
			if (in[t1]>in[t2]) swap(t1,t2);
			res+=query(1,1,n,in[t1],in[t2]);
			//cout << query(1,1,n,in[t1],in[t2]) << 'p';
			cout << res << '\n';
		}
		else{
			update(1,1,n,in[i.a],i.b);
		}
	}
}