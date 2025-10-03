#include<bits/stdc++.h>
using namespace std;

int tree[2][1<<20];

void update(int x,int i,int v){
	while (i< 1<<20){
		tree[x][i]+=v;
		i+=i&-i;
	}
}
int q(int i,int x,int k=0){
	while (x){
		k+=tree[i][x];
		x-=x&-x;
	}
	return k;
}
int query(int i,int x,int y){
	return q(i,y)-q(i,x-1);
}
int main(){
	cin.tie(0);cout.tie(0);
	ios::sync_with_stdio(false);
	int n;cin >> n;
	for (int i=0;i<n;i++){
		int x1,x2,x3,y1,y2,y3;
		cin >> x1 >> y1 >> x2 >> y2 >> x3 >> y3;
		if (max({x1,x2,x3})-min({x1,x2,x3})>1){
			update(0,min({x1,x2,x3})+1,1);
			update(0,max({x1,x2,x3}),-1);
		}
		if (max({y1,y2,y3})-min({y1,y2,y3})>1){
			update(1,min({y1,y2,y3})+1,1);
			update(1,max({y1,y2,y3}),-1);
		}
	}
	int w;cin >> w;
	while (w--){
		char a,b;
		int x;
		cin >> a >> b >> x;
		if (a=='x'){
			cout << q(0,x) <<'\n';
		}
		else{
			cout << q(1,x) <<'\n';
		}
	}
}