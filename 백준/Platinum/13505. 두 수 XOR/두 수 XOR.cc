#include<bits/stdc++.h>
using namespace std;
struct trie{
	trie *l,*r; // l -> 1 / r -> 0
	int v=0;
	trie(){l=r=NULL;v=0;}	
};

int query(trie *a,int d,int v){
	int res=0;
	for (int i=30;i>=0;i--){
		int b=(d>>i)&1;
		int ist=b^1;
		if (ist){
			if (a->l){
				res+=1<<i;
				a=a->l;
			}
			else{
				a=a->r;
			}
		}
		else{
			if (a->r){
				res+=1<<i;
				a=a->r;
			}
			else{
				a=a->l;
			}
		}
	}
	return res;
}

void update(trie *a,int d,int v){
	if (v==-1) return;
	int t=d&(1<<v);
	
	if (t){
		if (!a->l){
			a->l=new trie();
			a->l->v=1;
		}
		update(a->l,d,v-1);
	}
	else{
		if (!a->r){
			a->r=new trie();
		}
		update(a->r,d,v-1);
	}
	return;
}

int main(){
	cin.tie(0);cout.tie(0);
	ios::sync_with_stdio(false);
	int n;cin >>n;
	int res=0;
	trie *a;a=new trie();
	int x;cin >> x;update(a,x,30);
	for (int i=1;i<n;i++){
		cin >> x;
		res=max(res,query(a,x,30));
		update(a,x,30);
	}
	cout << res;
}