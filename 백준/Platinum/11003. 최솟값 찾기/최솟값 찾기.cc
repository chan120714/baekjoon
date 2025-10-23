#include<bits/stdc++.h>
using namespace std;
int main(){
	cin.tie(0);cout.tie(0);
	ios::sync_with_stdio(false);
	int n,m;
	cin >> n >> m;
	deque<pair<int,int> > q;
	for (int i=0;i<n;i++){
		int k;
		cin >>k;
		while (q.size() &&q.front().first<i-m+1){
			q.pop_front();
		}
		while (q.size() && q.back().second>=k){
			q.pop_back();
		}
		q.push_back({i,k});
		cout << q.front().second<<' ';
	}
}