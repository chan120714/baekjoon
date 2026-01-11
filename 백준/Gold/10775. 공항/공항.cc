#include<iostream>
using namespace std;
int visit[100000];
bool solve(int n){
	while (visit[n]){
		n-=visit[n]++;
		if (n<=0) return false;
	}
	visit[n]++;
	return true;
}
main(){
	cin.tie(0);cout.tie(0);
	ios::sync_with_stdio(false);
	int n,m,i;
	cin >> n >> m;
	for (i=0;i<m;i++){
		int k;
		cin >> k;
		if (solve(k)) continue;
		else break;
	}
	cout << i;
}