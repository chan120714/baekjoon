#include <bits/stdc++.h>
using namespace std;
/*Team.그게왜진조잘못이느냐?*/
using ll = long long int;
using tri = tuple<int, int, int>;
using pr = pair<double, int>;

vector<tri> p;
vector<pr> v[101010];

double dist[101010];
bitset<101010> visited;

int n,m,q;

double Dist(tri a, tri b) {
    auto [x0, y0, z0] = a;
    auto [x1, y1, z1] = b;
    double dx,dy,dz;
    dx=x0-x1;
    dy=y0-y1;
    dz=z0-z1;

    return sqrt(sqrt(dx*dx+dy*dy+dz*dz));
}

void dijkstra() {
    priority_queue<pr, vector<pr>, greater<pr>> pq;
    pq.push({0.0, 1});
    dist[1] = 0.0;
    for (int i = 2; i <= n; i++) dist[i] = 1e9;

    while (pq.size()) {
        auto [d, po] = pq.top(); pq.pop();

        if (visited[po]) continue;
        visited[po] = true;
        for (auto [nd, np]: v[po]) {
            if (dist[np] > d + nd) {
                dist[np] = d + nd;
                pq.push({d + nd, np});
            }
        }
    }
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    cout.setf(ios::fixed);
    cout.precision(12);

    cin >> n >> m >> q;

    p.push_back({0,0,0});
    for (int i = 1; i <= n; i++) {
        int x, y, z; cin >> x >> y >> z;
        p.push_back({x, y, z});
    }

    for (int i = 0; i < m; i++) {
        int a, b; cin >> a >> b;
        v[a].push_back({Dist(p[a], p[b]), b});
        v[b].push_back({Dist(p[a], p[b]), a});
    }

    dijkstra();

    while (q--) {
        int p1, t;
        cin >> p1 >> t;

        // cout << dist[p1] << "\n";

        if (dist[p1]*2>(double)t) cout << "impossible\n";
        else{
            cout << (double)t-sqrt(t*t-4*dist[p1]*dist[p1])  << '\n';
        }
    }

    return 0;
}