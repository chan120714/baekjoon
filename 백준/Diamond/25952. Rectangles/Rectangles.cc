#include <bits/stdc++.h>
using namespace std;

using ll = long long int;

ll n, ans;
vector<ll> v[101010];
vector<int> ptr; int siz;
int cnt[101010], k;
bitset<101010> chk1, chk2, chk3;

void sol1(int x){
	unordered_set<int> S;
	for (auto i:v[x]){
		S.insert(i);
	}
	for (int i = 0; i < 101010; i++) {
		if (i==x) continue;
    	if (cnt[i]>=200 && i<x) continue;
    	ll c=0;
    	for (auto j:v[i]){
    		if(S.find(j)!=S.end()) c++;
		}
		ans += c * (c - 1) / 2;
    }
}
void sol2(){
    map<pair<int, int>, ll> m;
    for (int i = 0; i < 101010; i++) {
        if (cnt[i] < 2) continue;
		if (cnt[i] >= 200) continue; 
        for (int j = 0; j < v[i].size(); j++) {
            for (int l = j + 1; l < v[i].size(); l++) {
                int x = v[i][j]; int y = v[i][l];
                if (x > y) swap(x, y);
                m[{x, y}]++;
            }
        }
    }

    for (auto i: m) {
        if (i.second >= 2) {
            ll x = i.second;
            ans += x * (x - 1) / 2;
        }
    }
}

int main() {
    ios_base::sync_with_stdio(0);
    cin.tie(0); cout.tie(0);

    cin >> n;
    for (int i = 0; i < n; i++) {
        int x, y; cin >> x >> y;

        v[x].push_back(y);
        cnt[x]++;
        if (cnt[x] == 1) ptr.push_back(x);
        k = max(k, cnt[x]);
    }
	sol2();
	for (int i=0;i<101010;i++){
	
	    if (cnt[i] >= 200) sol1(i);
	}
    cout << ans << '\n';

    return 0;
}