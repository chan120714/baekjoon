#include <bits/stdc++.h>
using namespace std;

#define x first
#define y second
using ll = long long int;
using Point = pair<ll, ll>;

Point operator+(Point p1, Point p2) { return {p1.x + p2.x, p1.y + p2.y}; }
Point operator-(Point p1, Point p2) { return {p1.x - p2.x, p1.y - p2.y}; }
ll operator*(Point p1, Point p2) { return p1.x * p2.x + p1.y * p2.y; }
ll operator/(Point p1, Point p2) { return p1.x * p2.y - p2.x * p1.y; }

int Sign(ll v) { return (v > 0) - (v < 0); } // 양수: +1, 0: 0, 음수: -1
ll Dist(Point p1, Point p2) { return (p2 - p1) * (p2 - p1); }

ll CCW(Point p1, Point p2, Point p3) { return Sign((p2 - p1) / (p3 - p1)); }

void SortCCW(vector<Point> &p) {
    sort(p.begin(), p.end());
    sort(p.begin() + 1, p.end(), [&](Point &p1, Point &p2) {
        ll dir = CCW(p[0], p1, p2);
        return dir ? dir > 0 : Dist(p[0], p1) < Dist(p[0], p2);
    });
}

vector<Point> ConvexHull(const vector<Point> &p) {
    vector<Point> hull;
    for (auto i: p) {
        while (hull.size() >= 2 && CCW(i, hull[hull.size()-2], hull[hull.size()-1]) <= 0) hull.pop_back();
        hull.push_back(i);
    }
    return hull;
}

int n;

int main() {
    ios_base::sync_with_stdio(0);
    cin.tie(0); cout.tie(0);

    cin >> n;
    vector<Point> p(n);
    for (int i = 0; i < n; i++) cin >> p[i].x >> p[i].y;

    SortCCW(p);
    vector<Point> hull = ConvexHull(p);
    int q;cin >> q;
    vector<Point> Query(q);
    for (int i=0;i<q;i++){
        int x;cin >> x;
        Query[i]={x,i};
    }
    sort(Query.begin(),Query.end());
    int v=0;
    Point res[340230];
    for (auto i:Query){
        ll x=i.x;
        while (x<hull[v].x || hull[v+1].x<x){v+=1;}
        ll val=hull[v].y*(hull[v+1].x-hull[v].x)+(hull[v+1].y-hull[v].y)*(x-hull[v].x);
        ll val1=(hull[v+1].x-hull[v].x);
        ll u=gcd(val,val1);
        res[i.y]={val/u,val1/u};
    }
    for (int i=0;i<q;i++){
        cout << res[i].x <<' '<<res[i].y <<'\n';
    }
    return 0;
}