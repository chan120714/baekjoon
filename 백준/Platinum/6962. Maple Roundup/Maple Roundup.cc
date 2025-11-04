#include<bits/stdc++.h>
using namespace std;
typedef long long ll;
struct d{
	int x,y;
};
int ccw(d x,d y,d z){
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
auto sol(vector<d> p){
	vector<d> s=make(p);
	int st,n=s.size();
	double res=987654;
	for (int i=0;i<n;i++){
		double cur=0;
		for (int st=0;st<n;st++){
			if (st==i || st==i+1) continue;
			int dx=s[i%n].y-s[(i+1)%n].y;
			int dy=s[(i+1)%n].x-s[i%n].x;
			int cc=abs(ccw(s[i],s[(i+1)%n],s[st]));
			cur=max(cur,(double)cc/dist(s[i],s[(i+1)%n]));
		}
		res=min(res,cur);
	}
	return res;
}
int main(){
    cin.tie(0);cout.tie(0);
    ios::sync_with_stdio(false);
    int T;cin >> T;
        while (T--){
        int n;
        cin >> n;
        vector<d> x(n);
        for (int i=0;i<n;i++){
            cin >> x[i].x >> x[i].y;
        }
        sort(x.begin(),x.end(),cmp);
        x=make(x);
        double res=0;
        for (int i=0;i<x.size()-1;i++){
            res+=sqrt((x[i].x-x[i+1].x)*(x[i].x-x[i+1].x)+(x[i].y-x[i+1].y)*(x[i].y-x[i+1].y));
        }
        res+=sqrt((x[x.size()-1].x-x[0].x)*(x[x.size()-1].x-x[0].x)+(x[x.size()-1].y-x[0].y)*(x[x.size()-1].y-x[0].y));
        cout << fixed << setprecision(2) << double(res) <<'\n';
    }
}
