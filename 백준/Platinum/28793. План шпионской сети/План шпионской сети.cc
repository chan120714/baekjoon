#include<bits/stdc++.h>
using namespace std;
typedef long long ll;
struct d{
	ll x,y,p;
};
ll ccw(d x,d y,d z){
	return (x.x*y.y+y.x*z.y+z.x*x.y)-(x.x*z.y+z.x*y.y+y.x*x.y);
}
int cccw(d w,d x,d y,d z){
	d p;
	p.x=z.x-(y.x-x.x);
	p.y=z.y-(y.y-x.y);
	return ccw(w,x,p);
}
auto make(vector<d> p){
	vector<d> up,down;
	for (auto i:p){
		while (up.size()>1 && ccw(up[up.size()-2],up.back(),i)>=0) up.pop_back();
		while (down.size()>1 && ccw(down[down.size()-2],down.back(),i)<=0) down.pop_back();
		up.push_back(i);
		down.push_back(i);
	}
	down.pop_back();
	reverse(down.begin(),down.end());
	down.pop_back();
	for (auto i:down){
		up.push_back(i);
	}
	return up;
}
bool cmp(d x,d y){
	if (x.x==y.x) return x.y<y.y;
	return x.x<y.x;
}
double dist(d x,d y){
	return sqrt((y.x-x.x)*(y.x-x.x)+(y.y-x.y)*(y.y-x.y));
}
int sdf[123123];
int main(){
    cin.tie(0);cout.tie(0);
    ios::sync_with_stdio(false);
    int T=1;
    while (T--){
        int n;
        cin >> n;
        vector<d> x(n);
        for (int i=0;i<n;i++){
            cin >> x[i].x >> x[i].y;
            x[i].p=i+1;
        }
        sort(x.begin(),x.end(),cmp);
        x=make(x);
        if (x.size()==n){
        	cout << 2 << '\n' << x[0].p<<' ' << x[2].p;
		}
		else{
			for (auto i:x){
				sdf[i.p]=1;
			}
			for (int i=1;i<=n;i++){
				if (!sdf[i]) {
					cout << 1 << '\n' << i;
					break;
				}
			}
		}
    }
}
