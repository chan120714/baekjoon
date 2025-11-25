#include<bits/stdc++.h>
int t[5432121],cnt[2132121];
using namespace std;
typedef long long ll;

vector<ll> era(int x){
	vector<ll> ret;
	for (int i=0;i<2000001;i++){
		t[i]=1;
	}
	for (int i=2;i<=1500;i++){
		if (t[i]==1){
			int j=2;
			while (i*j<=x){
				t[i*j]=0;
				j+=1;
			}
		}
	}
	for (int i=2;i<=x;i++){
		if (t[i]) ret.push_back(i);
	}
	return ret;
}

int tt[2021231];
int main(){
	cin.tie(0);cout.tie(0);
	ios::sync_with_stdio(false);
    int x;cin >> x;
    vector<int> a(x);
    auto c= era(2000000);
    for (int i=0;i<x;i++) cin >> a[i];
    int res=0;
    for(auto i:c){
        for (auto j:a){
			tt[j%i]++;
			res=max(tt[j%i],res);
        }
        for (auto j:a){
			tt[j%i]--;
        }
    }
    cout << res;
}