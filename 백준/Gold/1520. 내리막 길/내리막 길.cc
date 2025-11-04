#include<iostream>
#include<queue>
#include<vector>
using namespace std;
queue<pair<int,int > > q;
int graph[501][501],visited[501][501],val[501][501];
int n,m;
int main(){
	cin >> n >> m;
	val[0][0]=1;
	for (int i=0;i<n;i++)
	for (int j=0;j<m;j++){
		cin >> graph[i][j];
	}
	int dx[4]={1,-1,0,0},dy[4]={0,0,1,-1};
	for (int i=0;i<n;i++)
	for (int j=0;j<m;j++){
		for (int k=0;k<4;k++){
			int fx=i+dx[k],fy=j+dy[k];
			if (fx<0 || fy<0) continue;
			if (graph[i][j]>graph[fx][fy]){
				visited[fx][fy]+=1;
			}
		}
	}
	for (int i=0;i<n;i++)
	for (int j=0;j<m;j++) if(visited[i][j]==0) q.push({i,j});
	while (q.size()){
		int x,y;
		x=q.front().first;y=q.front().second;
		q.pop();
		for (int k=0;k<4;k++){
			int fx=x+dx[k],fy=y+dy[k];
			if (fx<0 || fy<0) continue;
			if (graph[x][y]>graph[fx][fy]){
				visited[fx][fy]-=1;
				val[fx][fy]+=val[x][y];
				if (visited[fx][fy]==0) q.push({fx,fy});
			}
		}
	}
	cout << val[n-1][m-1];
}
