#include<bits/stdc++.h>
using namespace std;
int n,arr[32][32];// 앞면 0 뒷면 1
int heu[32][32],res=987651234; 
struct Random {
	mt19937 rd;
	Random() : rd((unsigned)chrono::steady_clock::now().time_since_epoch().count()) {}
	int GetInt(int l = 0, int r = 32767) {
		return uniform_int_distribution<int>(l, r)(rd);
	}
	double GetDouble(double l = 0, double r = 1) {
		return uniform_real_distribution<double>(l, r)(rd);
	}
} Rand;
//https://m.blog.naver.com/jinhan814/222503424200

void flip(int x){
	for (int i=0;i<n;i++) arr[i][x]^=1;
}
// 평가함수
int result(){
	int res=0;
	for (int i=0;i<n;i++){
		int cur=0;
		for (int j=0;j<n;j++){
			cur+=arr[i][j];
		}
		res+=min(cur,n-cur);
	}
	return res;
}
double t=3,d=0.9999;
void SA(){
	int e1,e2;
	int ret[102];
	for (int i=0;i<100000;i++){
		e1=result();
		int a=Rand.GetInt(0,n-1);
		flip(a);
		ret[a]+=1;
		e2=result();
		double p=exp((e1-e2)/t);
		if (p<=Rand.GetDouble(0,1)) flip(a);
		res=min(res,result());
		t*=d;
	}
}
int main(){
	cin.tie(0);cout.tie(0);
	ios::sync_with_stdio(false);
	cin >>n;
	for (int i=0;i<n;i++)
	for (int j=0;j<n;j++){
		char a;cin >>a;
		if (a=='H') arr[i][j]=0;
		else arr[i][j]=1;
	}
	SA();
	cout << res;
	
}