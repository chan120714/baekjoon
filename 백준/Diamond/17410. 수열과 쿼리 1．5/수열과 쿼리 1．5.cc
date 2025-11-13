#import<iostream>
using namespace std;
int main(){cin.tie(0);ios::sync_with_stdio(false);int i,a,d,q,w,e,r,t=0;cin >> a;int g[a];for(int i=0;i<a;i++)cin>>g[i];cin>>d;while(d--){cin>>q>>w>>e;if(q>1){t=0;cin>>r;for(int j=w;j<=e;j++)if(g[j-1]>r)t+=1;cout<<t<<' ';}else g[w-1]=e;}}