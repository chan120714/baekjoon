#include<bits/stdc++.h>
using namespace std;

int tree[1312312];

void update(int x,int v){
	x+=1;
	while (x<=200000){
		tree[x]+=v;
		x+=x&-x;
	}
	return;
}

int query(int x){
	x+=1;
	int res=0;
	while (x){
		res+=tree[x];
		x-=x&-x;
	}
	return res;
}
int q(int x){
	int st=0,ed=100001;
	int res=-1;
	while (st<=ed){
		int mid=st + ed >> 1;
		if (query(mid)>=x){
			res=mid;
			ed=mid-1;
		}
		else{
			st=mid+1;
		}
	}
	return res;
}
int main(){
	cin.tie(0);cout.tie(0);
	ios::sync_with_stdio(false);
	int n,m;cin >> n >> m;
	
	for (int i=0;i<n;i++){
		int x;cin >> x;
		update(x,1);
	}
	vector<pair<int,int> > a(m);
	
	for (int i=0;i<m;i++) cin >> a[i].first;
	for (int i=0;i<m;i++) cin >> a[i].second;
	
	int res=1;
	
	for (auto i:a){
		int x=i.first,t=i.second;
		
		int y=q(n-t+1);
		
		if (y>=x){
			update(y,-1);
			update(y-x,1);
		}
		else{
			res=0;
			break;
		}
	}
	
	cout << res;
}