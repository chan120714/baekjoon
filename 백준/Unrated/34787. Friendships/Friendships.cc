#include <bits/stdc++.h>
using namespace std;

// #pragma GCC optimize("O3")
// #pragma GCC optimize("Ofast")
// #pragma GCC optimize("unroll-loops")

int n, q;
int c[404040], al[51], memo[404040][51];
vector<vector<int>> v;



int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    cin >> n >> q;
    for (int i = 1; i <= n; i++) c[i] = 0;
    al[0] = n;
    v.resize(n + 1);

    for(int i = 1; i <= n; i++) {
        memo[i][0] = 1;
        v[i].push_back(i);
    }

    while (q--) {
        char op;
        int x, y;
        cin >> op;

        if (op == 'F') {
            cin >> x >> y;
            v[x].push_back(y);
            v[y].push_back(x);
            memo[y][c[x]]++;
            memo[x][c[y]]++;
        }
        if (op == 'A') {
            cin >> x;

            al[c[x]]--;

            for(auto j : v[x]) {
                memo[j][c[x]]--;
                memo[j][c[x]+1]++;
            }

            c[x]++;
            
            al[c[x]]++;
        }
        if (op == 'Q') {
            cin >> x;
            
            int ans = -1;
            for (int i = 50; i >= 0; i--) {
                if(al[i] - memo[x][i] > 0) {
                    ans = i;
                    break;
                }
            }
            cout << ans << '\n';
        }
    }

    return 0;
}