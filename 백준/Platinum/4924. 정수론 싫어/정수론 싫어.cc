#include<bits/stdc++.h>
using namespace std;

int a[5050505];

void f(){
	for (int i=2;i<=1000000;i++){
		if (a[i]!=-1) continue;
		a[i]=-2;
		int j=i*2;
		while (j<=1000000){
			int k=j;
			while (k%i==0){
				k/=i;
				a[j]+=1;
			}
			j+=i;
		}
	}
}
int siz;
int seg[20101010];


int main(){
	cin.tie(0);cout.tie(0);
	ios::sync_with_stdio(false);
	for (int i=0;i<1010101;i++) a[i]=-1;
	f();
	int x,y;
	int T=1;
	while (1){
		cin >> x >> y;
		if (x+y==-2) break;
		int res=INT_MIN;
		int cur=0;
		for (int i=x;i<=y;i++){
			cur=max(cur+a[i],a[i]);
			res=max(res,cur);
		}
		cout << T++ << ". "<<res << '\n';
	}
}