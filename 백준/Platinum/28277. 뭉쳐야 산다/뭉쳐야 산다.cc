#include<bits/stdc++.h>
using namespace std;

vector<set<int>> a(510230);

int main(){
	cin.tie(0);cout.tie(0);
	ios::sync_with_stdio(false);
	int n,q;cin >> n >> q;
	for (int i=1;i<=n;i++){
		int T;cin >> T;
		while (T--){
			int x;cin >> x;
			a[i].insert(x);
		}
	}
	while (q--){
		int x;cin >> x;
		if (x==1){
			int w,e;cin >> w >> e;
			int A=a[w].size(),B=a[e].size();
			if (A<B){
				swap(a[w],a[e]);
			}
			for (auto i:a[e]){
				a[w].insert(i);
			}
			a[e].clear();
		}
		else{
			int A;cin >> A;
			cout << a[A].size()<<'\n';
		}
	}
}