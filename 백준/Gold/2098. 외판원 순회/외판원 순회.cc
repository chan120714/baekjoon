#include<bits/stdc++.h>
using namespace std;
int graph[16][16],visited[16][1<<16],n;
#define INF 23456789
int TSP(int x,int v){
	v|=(1<<x);
	if (v==(1<<n)-1){
		if (graph[x][0]>0) return graph[x][0];
		else return INF;
	}
	int&res=visited[x][v];
	if (res>0) return res;
	res=INF;
	for (int i=0;i<n;i++){
		if (graph[x][i]==0) continue;
		if (v&(1<<i)) continue;
		res=min(res,graph[x][i]+TSP(i,v));
	}
	return res;
}
int main(){
	cin.tie(0);cout.tie(0);
	ios::sync_with_stdio(false);
	cin >> n;
	for (int i=0;i<n;i++)
	for (int j=0;j<n;j++) cin >> graph[i][j];
	cout << TSP(0,0);
}