#include<bits/stdc++.h>
using namespace std;
 
int tree[123456];
int parent[123456];
 
struct q{
    int a,b,c,d;
    bool operator <(q x){
        if (b==x.b) return a<x.a;
        return b<x.b;
    }
};
 
void update(int i,int v){
    while (i<=100000){
        tree[i]+=v;
        i+=i&-i;
    }
}
 
int qq(int x){
    int res=0;
    while (x){
        res+=tree[x];
        x-=x&-x;
    }
    return res;
}
 
int query(int x,int y){
    return qq(y)-qq(x-1);
}
 
int find(int x){
    if (x==parent[x]) return x;
    return parent[x]=find(parent[x]);
}
 
void unioned(int x){
    parent[x]=find(x-1);
}
 
int main(){
    cin.tie(0);cout.tie(0);
    ios::sync_with_stdio(false);
 
    for (int i=0;i<123456;i++){
        parent[i]=i;
    }
    int n,k;cin >> n >> k;
    vector<int> a(n);
    vector<q> Q(k);
    for (int i=0;i<n;i++) cin>>a[i];
 
    for (int i=0;i<k;i++){
        cin >> Q[i].a >> Q[i].b >> Q[i].c;
        int ret=Q[i].c+Q[i].b-Q[i].a+1;
        Q[i].d=(ret>=0) ? (ret+1)/2 : ret/2;
        if (Q[i].d>Q[i].b-Q[i].a+1){
            cout << "Impossible";
            return 0;
        }
    }
 
    sort(Q.begin(),Q.end());
    vector<int> y(n+1),used(n+1);
    for (int i=1;i<=n;i++){
        if (a[i-1]==1){
            y[i]=1;
            used[i]=1;
            update(i,1);
            unioned(i);
        }
        else if (a[i-1]==-1){
            y[i]=0;
            used[i]=1;
            unioned(i);
        }
        else{
            y[i]=0;
            used[i]=0;
            parent[i]=i;
        }
    }
 
    for (auto i:Q){
        int cur=query(i.a,i.b);
        int need=i.d-cur;
        while (need>0){
            int p=find(i.b);
            if (p<i.a){
                cout << "Impossible";
                return 0;
            }
            y[p]=1;
            update(p,1);
            unioned(p);
            need-=1;
        }
    }
    for (int i=1;i<=n;i++){
        cout << 2*y[i]-1 << ' ';
    }
}