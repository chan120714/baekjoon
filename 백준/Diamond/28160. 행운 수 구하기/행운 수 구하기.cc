#include <bits/stdc++.h>
using namespace std;

#pragma GCC optimize("O3")
#pragma GCC optimize("Ofast")
#pragma GCC optimize("unroll-loops")

const int MAX = 54790233; // 3 * 10^6번째 값
typedef unsigned long long ull;
typedef long long ll;

int ans[3030303];
int cnt = 5;
int N = MAX / 2 +1;
int W = (N + 63) >> 6;
vector<int> st;
int tmp;

struct Fenwick {
	vector<int> tree; int sz;
	Fenwick(int sz) : sz(sz), tree(sz + 1) {}
	void Update(int i, int val) {
		for (; i <= sz; i += i & -i) tree[i] += val;
	}
	int Query(int i) {
		int ret = 0;
		for (; i; i -= i & -i) ret += tree[i];
		return ret;
	}
	pair<int,int> Kth(int k) {
		int ret = 0,ac=0;
		for (int i = 31-__builtin_clz(sz); ~i; i--) {
			int t = ret | 1 << i;
			if (t <= sz && ac+tree[t] < k) {
				ret=t;ac+=tree[t];
			}
		}
		return {ret + 1,ac};
	}
};

bool ist(vector<ull>& b,int i){
	int o=i-1;
	return (b[o>>6]>>(o&63))&1ull;
}
void cb(vector<ull>& b,int i){
	int o=i-1;
	b[o>>6]&=~(1ull<<(o&63));
}
int sel(ull w,int k){
	while (1){
		int z=__builtin_ctzll(w);
		if (--k==0) return z;
		w&=w-1;
	}
}

void rm(vector<ull> &b,int l){
	int c=0;
	for (int w=0;w<W;w++){
		ull x=b[w];
		ull y=x;
		if (!y) continue;
		while (y){
			int z=__builtin_ctzll(y);
			if (++c==l){
				x&=~(1ull<<z);
				c=0;
			}
			y&=y-1;
		}
		b[w]=x;
	}
}

int main() {
    ios_base::sync_with_stdio(0);
    cin.tie(0); cout.tie(0);

    ans[1] = 1; ans[2] = 3; ans[3] = 7; ans[4] = 9; ans[5] = 13;
    ans[6] = 15; ans[7] = 21; ans[8] = 25; ans[9] = 31; ans[10] = 33;
    cnt = 10;
	Fenwick fw(W);
	vector<ull> aaa(W,~0ull);
	if (N-((W-1)<<6)<64) aaa[W-1]= (1ull<<(N-((W-1)<<6)))-1ull;
	
	for (int i = 3; i <= N; i+=3){
		cb(aaa,i);
	}
    for (int i = 3; i <= 10; i++) {
        rm(aaa,ans[i]);
    }
    int tot=0;
    for (int i=0;i<W;i++){
    	int c=__builtin_popcountll(aaa[i]);
    	fw.Update(i+1,c);
    	tot+=c;
	} 
    
    for (int i = 35; cnt < 3000000; i += 2) {
    	if (i>MAX) break;
        if (!ist(aaa,(i+1)>>1)) continue;
        ans[++cnt] = i;
		
		int j=i;
        while (j <= tot){
        	auto [a,b]=fw.Kth(j);
        	ull x=aaa[a-1];
			int pos=sel(x,j-b);
			aaa[a-1]=x&~(1ull<<pos);
			fw.Update(a,-1);
        	tot-=1;
        	j+=i-1;
		}
    }
    
    int x,y;cin >> x >> y;
    for (int i=x;i<=y;i++){
    	cout << ans[i] << '\n';
	}

    return 0;
}