#include<bits/stdc++.h>
using namespace std;
int va[2012],vb[2132];
int tree[14212];
void update(int n,int s,int e,int i,int v){
    if (i<s || e<i) return;
    if (s==e){
        tree[n]=max(tree[n],v);
        return;
    }
    update(n*2,s,(s+e)/2,i,v);
    update(n*2+1,(s+e)/2+1,e,i,v);
    tree[n]=max(tree[n<<1],tree[n<<1 |1]);
}

int query(int n,int s,int e,int l,int r){
    if (e<l || r<s)return 0;
    if (l<=s && e<=r) return tree[n];
    return max(query(n*2,s,(s+e)/2,l,r),query(n*2+1,(s+e)/2+1,e,l,r));
}
int main(){
    cin.tie(0);cout.tie(0);
    ios::sync_with_stdio(false);
    int n,m;cin >> n >> m;
    vector<int> a(n),b(m);

    for (int i=0;i<n;i++) cin >> a[i];
    for (int i=0;i<m;i++) cin >> b[i];

    for (int i=1;i<=n;i++){
        va[a[i-1]]=i;
    }
    for (int i=1;i<=m;i++){
        vb[b[i-1]]=i;
    }
    int q;cin >> q;
    vector<pair<int,int> > t(q);
    for (int i=0;i<q;i++){
        int x,y;cin >>x>>y;
        t[i].first=va[x];
        t[i].second=-vb[y];
    }
    sort(t.begin(),t.end());

    for (int i=0;i<q;i++){
        update(1,0,2000,-t[i].second,1+query(1,0,2000,0,-t[i].second-1));
        //cout << t[i].first << ' ' << -t[i].second << '\n';
    }
    cout << q-query(1,1,2000,1,2000);
}