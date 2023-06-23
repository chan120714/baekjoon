#include<bits/stdc++.h>
using namespace std;
int main(){
	int a,k,d,q,w,e,r,t=0;
	scanf("%d",&a);
	int graph[a];
	for (int i=0;i<a;i++){
		scanf("%d",&k);
		graph[i]=k;
	}
	scanf("%d",&d);
	for (int i=0;i<d;i++){
		scanf("%d",&q);
		if (q==2){
			t=0;
			scanf("%d %d %d",&w,&e,&r);
			for (int j=w;j<=e;j++){
				if (graph[j-1]>r){
					t+=1;
				}
			}
			printf("%d\n",t);
		}
		else{
			scanf("%d %d",&w,&e);
			graph[w-1]=e;
		}
	}
}