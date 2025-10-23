#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
typedef pair<ll,ll> pll;
const ll MAX=1000000000000000000;
struct Node{
    Node *l,*r;
    int num;
    Node(){
        l=r=NULL;
        num=0;
    }
};
void update(Node *n,ll s,ll e,ll v){
    if (s==e){
        n->num+=1;
        return;
    } 
    if (v<=(s+e)/2){
        if (!n->l) n->l=new Node();
        update(n->l,s,(s+e)/2,v);
        n->num+=1;
        return;
    }
    else{
        if (!n->r) n->r=new Node();
        update(n->r,(s+e)/2+1,e,v);
        n->num+=1;
        return;
    }
}
int query(Node *n,ll s,ll e,ll v){
    if (s==e) return n->num;
    if (v<=(s+e)/2){
        if (!n->l) return 0;
        else return query(n->l,s,(s+e)/2,v);
    }
    else{
        if (!n->r) return 0;
        else return query(n->r,(s+e)/2+1,e,v);
    }
}
struct tt{
    ll x;
    int dist;
    bool ve;
};
Node *root=new Node();
int res[567896]={0,};
int main(){
    cin.tie(0);cout.tie(0);
    ios::sync_with_stdio(false);
    ll l,n,k;cin >> l>> n >> k;
    vector<ll> a(n);
    for (int i=0;i<n;i++) cin >> a[i];
    queue<tt> t;
    ll ret=0;
    for (auto i:a){
        t.push({i+1,1,1});
        t.push({i-1,1,0});
        res[0]+=1;
        update(root,0,MAX,i);
        ret+=1;
    }
    while (ret<k){
        ll x=t.front().x;
        int dist=t.front().dist;
        bool ve=t.front().ve;
        t.pop();
        if (x<0 || x>l) continue;
        if (query(root,0,MAX,x))continue;
        update(root,0,MAX,x);
        res[dist]+=1;
        dist++;
        if (ve) x+=1;
        else x-=1;
        t.push({x,dist,ve});
        ret+=1;
    }
    int p=0;
    for (int i=0;i<530000;i++){
        for (int j=0;j<res[i];j++){
            cout << i<<'\n';
            p++;
            if (p==k){
                return 0;
            }
        }
    }
}