#include<bits/stdc++.h>
using namespace std;
int a[1233451];

int main(){
	int n,res=0;cin >> n;
	while (n--){
		int x;cin >> x;
		a[x]=max(a[x],a[x-1]+1);
	}
	for (int i=1;i<=1000001;i++){
		res=max(res,a[i]);
	}
	cout << res;
}