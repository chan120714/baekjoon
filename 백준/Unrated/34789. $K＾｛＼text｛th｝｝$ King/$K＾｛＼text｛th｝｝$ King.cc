#include <bits/stdc++.h>
using namespace std;

using ll = long long int;

ll n;
ll a[202020];
ll ps[202020];

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    cin >> n;

    for (int i = 1; i <= n; i++) cin >> a[i];
    sort(a + 1, a + n + 1);

    for (int i = 1; i <= n; i++) {
        ps[i] = ps[i-1] + a[i];
    }

    for (int i = n; i >= 1; i--) {
        int mid = i / 2 + 1;
        
        ll l = (ps[i] - ps[mid]) - (a[mid] * (i - mid));
        //cout << ps[n] - ps[mid] << '\n';
        //cout << l << '\n';
        ll r = (a[mid] * mid) - ps[mid];
        //cout << r << '\n';
        cout << l + r << '\n';
    }

    return 0;
}