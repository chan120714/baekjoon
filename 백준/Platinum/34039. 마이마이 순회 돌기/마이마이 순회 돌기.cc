#include<bits/stdc++.h>
using namespace std;
typedef long long ll;
typedef pair<ll,ll> pll;

const int MAX=424288;

vector<ll> query;

struct node{
	ll cnt,sum;
}tree[MAX*4];

struct upd{
	ll ai,val,idx;
	bool operator <(upd &x){
		if (ai==x.ai){
			if (val==x.val) return idx<x.idx;
			return val<x.val;
		}
		return ai<x.ai;
	}
}update[MAX];

vector<upd> a;
int arr[MAX];
bool type[MAX];


node merge(node a,node b){
	return {a.cnt+b.cnt,a.sum+b.sum};
}


void seg_update(int n,int s,int e,int idx,int val){
	if (idx<s || e<idx) return;
	if (s==e){
		tree[n]={1,val};
		return;
	}
	seg_update(n*2,s,(s+e)/2,idx,val);
	seg_update(n*2+1,(s+e)/2+1,e,idx,val);
	tree[n]=merge(tree[n*2],tree[n*2+1]);
	return;
}

void seg_update1(int n,int s,int e,int idx,int val){
	if (idx<s || e<idx) return;
	if (s==e){
		tree[n]={0,0};
		return;
	}
	seg_update1(n*2,s,(s+e)/2,idx,val);
	seg_update1(n*2+1,(s+e)/2+1,e,idx,val);
	tree[n]=merge(tree[n*2],tree[n*2+1]);
	return;
}

int seg_query(int n,int s,int e,ll v){
	if (s==e){
		if (tree[n].sum<=v) return tree[n].cnt;
		return 0;
	} 
	if (tree[n*2].sum<v) return tree[n*2].cnt+seg_query(n*2+1,(s+e)/2+1,e,v-tree[n*2].sum);
	return seg_query(n*2,s,(s+e)/2,v); 
}

int squery(int n,int s,int e,int l,int r){
	if (e<l || r<s) return 0;
	if (l<=s && e<=r) return tree[n].sum;
	return squery(n*2,s,(s+e)/2,l,r)+squery(n*2+1,(s+e)/2+1,e,l,r);
}

int main(){
	cin.tie(0);cout.tie(0);
	int n,T;cin >> n >> T;
	
	for (int i=1;i<=n;i++){
		cin >> arr[i];
		a.push_back({arr[i],0,i});
	}
	int idx=1;
	for (int j=0;j<T;j++){
		int x;cin >> x;
		if (x==1){
			int i,v; cin >> i >> v;
			a.push_back({v,idx,0});
			update[idx]={v,i,idx};
			idx+=1;
		}
		else if (x==2){
			ll k;cin >> k;
			query.push_back(k);
		}
		else{
			int v;cin >> v;
			n+=1;
			arr[n]=1000000007;
			a.push_back({arr[n],0,n});
			a.push_back({v,idx,0});
			update[idx]={v,n,idx};
			idx+=1;
		}
		type[j]=x&1;
	}
	sort(a.begin(),a.end());
	for (int i=0;i<a.size();i++){
		if (a[i].val){
			update[a[i].val].idx=i+1;
		}
		else{
			arr[a[i].idx]=i+1;
			seg_update(1,1,MAX,i+1,a[i].ai);
		}
	}
	int idx1=0,idx2=1;
	//for (int i=1;i<=3;i++) cout << update[i].ai << ' '<< update[i].idx << ' ' << update[i].val << '\n';
	//for (int i=0;i<7;i++) cout << a[i].ai << ' '<< a[i].idx << ' ' << a[i].val << '\n';
	//for (int i=0;i<3;i++) cout << query[i] << ' ';
	//cout << '\n';
	for (int i=0;i<T;i++){
		if (!type[i]){
			cout << seg_query(1,1,MAX,query[idx1]) << '\n';
			idx1+=1;
		}
		else{
			seg_update1(1,1,MAX,arr[update[idx2].val],0);
			seg_update(1,1,MAX,update[idx2].idx,update[idx2].ai);
			arr[update[idx2].val]=update[idx2].idx;
			idx2+=1;
		}
		/*for (int i=1;i<=n;i++) cout << arr[i] << ' ';
		cout << squery(1,1,MAX,1,5);
		cout << '\n';*/
	}
}

