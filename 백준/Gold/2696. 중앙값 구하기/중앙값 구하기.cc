#include<bits/stdc++.h>
using namespace std;
#include <ext/pb_ds/assoc_container.hpp>
#include <ext/pb_ds/tree_policy.hpp>
using namespace __gnu_pbds;
#define ordered_set tree<int, null_type, less_equal<int>, rb_tree_tag,tree_order_statistics_node_update>

int main(){
	cin.tie(0);cout.tie(0);
	ios::sync_with_stdio(false);
	int T;cin >> T;
	while (T--){
		int n;cin >> n;
		cout << (n+1)/2 << '\n';
		ordered_set a;
		for (int i=0;i<n;i++){
			int x;cin >> x;
			a.insert(x);
			if (i%2==0){
				cout << *(a.find_by_order(i/2)) <<' ';
			}
		}
		cout << '\n';
	}
}