#include<bits/stdc++.h>
using namespace std;
typedef unsigned int ui;
typedef long long ll;
typedef pair<int,int> pi;
typedef pair<ll,ll> pll;

bool t[101010101];
void era(int x){
	vector<int> ret;
	for (int i=2;i<=10000;i++){
		if (t[i]==0){
			int j=2;
			while (i*j<=x){
				t[i*j]=1;
				j+=1;
			}
		}
	}
}

int main(){
    cin.tie(0);cout.tie(0);
    ios::sync_with_stdio(false);
    int n;cin >> n;
    era(100000000);
    ui res=1;
    for (ll i=2;i<=n;i++){
        if (!t[i]){
            ll k=i;
            while (k*i<=n){
                k*=i;
            }
            res*=k;
        }
    }
    cout << res;
    return 0;
}