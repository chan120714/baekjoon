#include <bits/stdc++.h>
using namespace std;

int main(){
    int n,k;cin >> n >> k;
    int a=0,b=1,c=1,d=n;
    if (k == 1){
		cout << a << ' ' << b << '\n';
		return 0;
	}
    int idx=2;
    if (k == 2){
		cout << c << ' ' << d << '\n';
		return 0;
	}

    while (c<=n){
        int t=(n+b)/d;
        int e=t*c-a;
        int f=t*d-b;
        a=c;b=d;c=e;d=f;
        idx+=1;
        if (idx==k){
        	cout << c <<' ' << d <<'\n';
        	return 0;
		}
    }
}
