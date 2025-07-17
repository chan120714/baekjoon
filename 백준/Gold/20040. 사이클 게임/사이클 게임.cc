#include<bits/stdc++.h>
using namespace std;
int parent[523456];

int find(int x){
	if (x==parent[x]) return x;
	return parent[x]=find(parent[x]);
}

void unioned(int x,int y){
	x=find(x);
	y=find(y);
	if (x>y) swap(x,y);
	parent[y]=x;
	return;
}

int main(){
	cin.tie(0);cout.tie(0);
	ios::sync_with_stdio(false);
	for (int i=0;i<512312;i++) parent[i]=i;
	int n,m;cin >> n >> m;
	int res=0;
	for (int i=1;i<=m;i++){
		int x,y;cin >> x >> y;
		if (find(x)==find(y)){
			res=i;break;
		}
		unioned(x,y);
	}
	cout << res;
}