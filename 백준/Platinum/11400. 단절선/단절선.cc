#include<bits/stdc++.h>
using namespace std;

typedef long long ll;
typedef pair<ll,ll> pll;
typedef pair<int,int> pii;

const int MX=102121;
vector<int> graph[MX]; // 인접 리스트
int num[MX]; // 방문하는 정점에 번호 부여
int cnt;
int par[MX];
int low[MX];
// low[x] : x 혹은 x의 자손에서 Backward Edge를 타고 올라갈 수 있는 가장 높은 정점의 num 값
// 다른 말로는 Backward Edge를 타고 올라가 얻을 수 있는 최소의 num 값

vector<pii> Bridge;

void dfs(int x) {
    num[x] = ++cnt;
    // low의 초깃값
    low[x] = num[x];
    for(int nxt : graph[x]){
        if(nxt == par[x]) continue;
        // Tree Edge인 경우
        if(!num[nxt]){
            par[nxt] = x;
            dfs(nxt);
 
            if(num[x] < low[nxt]){
                Bridge.push_back({min(x, nxt), max(x, nxt)});
            }
            low[x] = min(low[x], low[nxt]);
        }
        // Backward Edge인 경우
        else{
            low[x] = min(low[x], num[nxt]);
        }
    }
}

int main(){
	cin.tie(0);cout.tie(0);
	ios::sync_with_stdio(false);
	int v,e;cin >> v >> e;
	
	for (int i=1;i<=e;i++){
		int x,y;cin >>x >> y;
		graph[x].push_back(y);
		graph[y].push_back(x);
	}
	
	for (int i=1;i<=v;i++){
		if (!num[i])dfs(i);
	}

	sort(Bridge.begin(),Bridge.end());
	cout << Bridge.size() << '\n';
	for (auto i:Bridge){
		cout << i.first << ' ' << i.second << '\n';
	}
	
}