#include<bits/stdc++.h>
using namespace std;
int n,m,x,y;
vector<int> a,b;

bool f(int A){
	multiset<int> c;
	int j=0;
	
	for (int i=0;i<n;i++){
		while (j<m && b[j]<=a[i]){
			c.insert(b[j]);
			j++;
		}
		int v=i<A ? y : x;
		while (v && c.size()){
			c.erase(prev(c.end()));
			v--;
		}
	}
	
	return (j==m && c.empty());
}
int main(){
	cin.tie(0);cout.tie(0);
	ios::sync_with_stdio(false);
	cin >> n >> m >> x >> y;
	a.resize(n);
	b.resize(m);
	
	for (int i=0;i<n;i++) cin >> a[i];
	for (int i=0;i<m;i++) cin >> b[i];
	
	sort(a.begin(),a.end());
	sort(b.begin(),b.end());
	
	if (!f(0)){
		cout << "impossible";
	}
	else{
		int st=0,ed=n;
		while (st<ed){
			int mid=(st+ed+1) >> 1;
			if (f(mid)) st= mid;
			else ed=mid-1;
		}
		cout << st;
	}
}