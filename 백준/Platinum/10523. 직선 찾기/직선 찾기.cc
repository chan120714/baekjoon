#include<bits/stdc++.h>
using namespace std;
#define y second
#define x first
typedef long long ll;
typedef pair<ll,ll> p;
ll ccw(p x1,p x2,p x3){
	return (x1.x*x2.y+x2.x*x3.y+x3.x*x1.y-x1.x*x3.y-x3.x*x2.y-x2.x*x1.y);
}

int main(){
    cin.tie(0);cout.tie(0);
    ios::sync_with_stdio(false);
    int n,po;cin >> n >> po;
    vector<p> a(n);
    for (int i=0;i<n;i++){
        cin >> a[i].x >> a[i].y;
    }
    mt19937 engine((unsigned int)time(NULL));
    uniform_int_distribution<int> distribution(0, 2147483647);
    auto generator = bind(distribution, engine);
    int T=5000,ist=0;
    while (T--){
        int x=generator()%n,y=generator()%n;
        if (x==y){
            y+=1;
            y%=n;
        }
        int res=2;
        for (int i=0;i<n;i++){
            if (i==x || i==y) continue;
            if (ccw(a[i],a[x],a[y])==0) res+=1;
        }
        if (res*100-n*po>=0){
            ist=1;
            break;
        }
    }

    if (!ist){
        cout <<"im";
    }
    cout <<"possible";
}