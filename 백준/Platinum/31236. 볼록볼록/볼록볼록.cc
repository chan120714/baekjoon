#include<bits/stdc++.h>
typedef long long ll;
using namespace std;
struct p{
	ll x,y;
};
ll ccw(p x1,p x2,p x3){
	return (x1.x*x2.y+x2.x*x3.y+x3.x*x1.y-x1.x*x3.y-x3.x*x2.y-x2.x*x1.y);
}


int main(){
    cin.tie(0);cout.tie(0);
    ios::sync_with_stdio(false);
    
    int n;cin >> n;
    int st=0,ed=2,res=0;
    vector<p> a(n);
    for (int i=0;i<n;i++){
        cin >> a[i].x >> a[i].y;
    }
    for (;ed<n;ed++){
        if (ed-st<2){
            continue;
        }
        if (ccw(a[ed-2],a[ed-1],a[ed])<=0){
            st=ed-1;
            continue;
        }
        while (ccw(a[ed-1],a[ed],a[st])<=0 || ccw(a[ed],a[st],a[st+1])<=0){
            st+=1;
        }
        res=max(res,ed-st+1);
    }
    cout << (res > 2 ? res : -1);
}