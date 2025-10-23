#include<bits/stdc++.h>
using namespace std;

int a[101212];

int main(){
	cin.tie(0);cout.tie(0);
	ios::sync_with_stdio(false);
	for (int i=1;i<=100000;i++){
		int j=i,res=0;
		while (j){
			res+=j%10;
			j/=10;
		}
		a[i]=res;
	}
	
	int T;cin >> T;
	
	while (T--){
		int n,res=-1;cin >> n;
		for (int i=n;i<=n+100;i++){
			if (a[i/100000]+a[i%100000]+n==i){
				res=i;
				break;
			}
		}
		cout << res << ' ';
	}
}