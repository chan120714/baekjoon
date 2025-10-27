#include<bits/stdc++.h>
using namespace std;
int a[4234512],parent[4321233];

int find(int x){
	if (x==parent[x]) return x;
	return parent[x]=find(parent[x]);
}

void unioned(int x,int y){
	x=find(x);
	y=find(y);
	if (x>y) swap(x,y);
	parent[x]=y;
	return;
}
int main(){
	cin.tie(0);cout.tie(0);
	ios::sync_with_stdio(false);
	for (int i=0;i<=4012312;i++) parent[i]=i;
	int n,m,k;cin >> n >> m >> k;
	for (int i=1;i<=m;i++){
		int x;cin >> x;
		a[x]+=1;
	}
	for (int i=1;i<=n;i++){
		if(a[i]==0) unioned(i,i+1);
	}
	while (k--){
		int x;cin >> x;
		int t=find(x+1);
		cout << t << ' ';
		a[t]-=1;
		if (a[t]==0){
			unioned(t,t+1);
		}
	}
}