#include<bits/stdc++.h>
using namespace std;
typedef long long ll;

ll comb(ll n){
    return n*(n-1) >> 1;
}

int rpar[342123];
vector<int> graph[341231];

void dfs(int x,int r){
    for (auto i:graph[x]){
        if (i!=r){
            rpar[i]=x;
            dfs(i,x);
        }
    }
}
int parent[321321],val[321321];
int find(int x){
    if (x==parent[x]) return x;
    else return parent[x]=find(parent[x]);
}

void unioned(int x,int y){
    x=find(x);
    y=find(y);

    if (x==y) return;
    if (x>y) swap(x,y);
    parent[y]=x;
    val[x]+=val[y];
    val[y]=0;
}

int main(){
    cin.tie(0);cout.tie(0);
    ios::sync_with_stdio(false);
    int n;cin >> n;

    for (int i=1;i<n;i++){
        int x,y;cin >> x >> y;
        graph[x].push_back(y);
        graph[y].push_back(x);
    }
    dfs(1,-1);

    for (int i=1;i<=n;i++){
        val[i]=1;
        parent[i]=i;
    }
    int q;cin >> q;
    while (q--){
        int k;cin >> k;
        ll res=0;
        vector<int> s(k);
        for (int i=0;i<k;i++) cin >> s[i];

        unordered_set<int> Set;

        for (int i=0;i<k;i++) Set.insert(s[i]);

        for (int i=0;i<k;i++){
            if (Set.find(rpar[s[i]])!=Set.end()){
                unioned(s[i],rpar[s[i]]);
            }
        }

        for (int i=0;i<k;i++){
            res+=comb(val[s[i]]);
        }

        for (int i=0;i<k;i++){
            val[s[i]]=1;
            parent[s[i]]=s[i];
        }
        cout << res  << '\n';
    }
}