#include<bits/stdc++.h>
using namespace std;
typedef unsigned long long ull;
typedef long long ll;
#define all(n) n.begin(),n.end()
//https://github.com/kth-competitive-programming/kactl/blob/main/content/number-theory/ModMulLL.h
ull modmul(ull a, ull b, ull M) {
	ll ret = a * b - M * ull(1.L / M * a * b);
	return ret + M * (ret < 0) - M * (ret >= (ll)M);
}
ull modpow(ull b, ull e, ull mod) {
	ull ans = 1;
	for (; e; b = modmul(b, b, mod), e /= 2)
		if (e & 1) ans = modmul(ans, b, mod);
	return ans;
}
//https://github.com/kth-competitive-programming/kactl/blob/main/content/number-theory/MillerRabin.h
bool isPrime(ull n) {
	if (n < 2 || n % 6 % 4 != 1) return (n | 1) == 3;
	ull A[] = {2, 325, 9375, 28178, 450775, 9780504, 1795265022},
	    s = __builtin_ctzll(n-1), d = n >> s;
	for (ull a : A) {   // ^ count trailing zeroes
		ull p = modpow(a%n, d, n), i = s;
		while (p != 1 && p != n - 1 && a % n && i--)
			p = modmul(p, p, n);
		if (p != n-1 && i != s) return 0;
	}
	return 1;
}
ull pollard(ull n) {
	auto f = [n](ull x) { return modmul(x, x, n) + 1; };
	ull x = 0, y = 0, t = 30, prd = 2, i = 1, q;
	while (t++ % 40 || __gcd(prd, n) == 1) {
		if (x == y) x = ++i, y = f(x);
		if ((q = modmul(prd, max(x,y) - min(x,y), n))) prd = q;
		x = f(x), y = f(f(y));
	}
	return __gcd(prd, n);
}
vector<ull> factor(ull n) {
	if (n == 1) return {};
	if (isPrime(n)) return {n};
	ull x = pollard(n);
	auto l = factor(x), r = factor(n / x);
	l.insert(l.end(), all(r));
	return l;
}
int main(){
	int n,res=0,cur=0;
	cin.tie(0);cout.tie(0);
	ios::sync_with_stdio(false);
	cin >> n;
	vector<ull> m(n);
	for (int i=0;i<n;i++) cin >> m[i];
	unordered_set<ull> pri;
	for (auto &i:m){
		vector<ull> pp=factor(i);
		for (auto &j:pp) pri.insert(j);
	}
	for (auto &i:pri){
		for (auto &j:m){
			if (j%i==0) cur++;
			else{
				res^=cur;
				cur=0;
			}
		}
		res^=cur;
		cur=0;
	}
	if (res) cout <<"First";
	else cout <<"Second";
}