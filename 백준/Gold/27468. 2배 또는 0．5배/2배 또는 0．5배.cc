#include<bits/stdc++.h>
using namespace std;
int main(){
	int n;cin >> n; 
	cout << "YES\n";
	if (n%2){
		for (int i=1;i<=n;i++){
			if (i%2) cout << (i+1)/2+i/4*2 << ' ';
			else cout << (i+4)/2+(i-1)/4*2 << ' ';
		}
	}
	else{
		for (int i=2;i<=n;i+=2){
			if (i%4){
				cout << i <<' '<<i-1 <<' ';
			}
			else cout << i-1<< ' ' <<i <<' '; 
		}
	}
}