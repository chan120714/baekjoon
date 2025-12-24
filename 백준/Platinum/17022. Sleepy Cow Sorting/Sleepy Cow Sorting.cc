#include<bits/stdc++.h>
using namespace std;

int tree[1231212];

void update(int i,int v){
	while (i<=120312){
		tree[i]+=v;
		i+=i&-i;
	}
}

int q(int x){
	int res=0;
	while (x){
		res+=tree[x];
		x-=x&-x;
	}
	return res;
}

int query(int x,int y){
	return q(y)-q(x-1);
}



int main(){
	cin.tie(0);cout.tie(0);
	ios::sync_with_stdio(false);
	
	int n;cin  >> n;
	vector<int> p(n);
	
	for (int i=0;i<n;i++) cin >> p[i];
	
	
	int k=n-1;
	while (k && p[k-1]<p[k]) k--;
	cout << k << '\n';
	if (k==0){
		return 0;
	}
	
	for (int i=k;i<n;i++) update(p[i],1);
	
	
	for (int i=0;i<k;i++){
		int x=p[i];
		int K=(k-1-i)+q(x-1);
		cout << K << ' ';
		update(x,1);
	}
}