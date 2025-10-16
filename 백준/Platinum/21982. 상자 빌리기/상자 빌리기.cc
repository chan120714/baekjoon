#include <bits/stdc++.h>
using namespace std;
int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);
    int t;
    cin >> t;
    while (t--) {
        int n, x;
        cin >> n >> x;
        long long hs, ha, hb, hc;
        long long ws, wa, wb, wc,res=-1;
        cin >> hs >> ha >> hb >> hc;
        cin >> ws >> wa >> wb >> wc;

        vector<long long> H(n), W(n);
        H[0] = hs % hc + 1;
        W[0] = ws % wc + 1;
        for (int i=1; i<=n-1; i++) {
            H[i] = H[i-1] + 1 + (H[i-1] * ha + hb) % hc;
            W[i] = (W[i-1] * wa + wb) % wc + 1;
        }
		deque<pair<long long ,long long > > q;
		for (int i=0;i<n;i++){
			long long cur=-H[i]*W[i];
			while (q.size() &&q.front().first<H[i]-x){
				q.pop_front();
			}
			if (q.size()) res=max(res,-cur-q.front().second);
			while (q.size() && q.back().second>=cur){
				q.pop_back();
			}
			q.push_back({H[i],cur});
			
		}
		cout << res << '\n';
    }
    return 0;
}
