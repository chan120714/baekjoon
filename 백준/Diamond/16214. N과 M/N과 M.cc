#include<stdio.h>
#define ll long long
ll pow(int x, int y, int p){
	x%=p;
	ll t;
	if (y==0){
		return 1;
	}
	if (y==1){
		return x%p;
	}
	t=pow(x,y/2,p);
	if (y%2){
		return (t*t)%p*x%p;
	}
	else{
		return (t*t)%p;
	}
}

ll phi(int n){
	ll res=n;
	for (int i=2;i*i<=n;i++){
		if (n%i==0){
			res-=(res/i);
			while (n%i==0){
				(n/=i);
			}
		}
	}
	if (n>1){
		res-=res/n;
	}
	return res;
}

int sol(int n, int m){
	int s=1;
	ll p[100]={m};
	for (int i=1;i<100;i++){
		p[i]=phi(p[i-1]);
		if (p[i]==1){
			s=i;
			break;
		}
	}
	int arr[100]={0};
	arr[s]=1;
	for (int i=s-1;i>0;i--){
		arr[i]=pow(n,arr[i+1],p[i])+p[i];
	}
	arr[0]=pow(n,arr[1],m);
	return arr[0];
}

int main(){
	int n,m,a;
	scanf("%d",&a);
	for (int i=0;i<a;i++){
		scanf("%d %d",&n,&m);
		if (m==1){
			printf("0\n");
		}
		else if (m==2){
			printf("%d\n",n%2);
		}
		else if (n==1){
			printf("1\n");
		}
		else{
			printf("%d\n",sol(n,m));
		}
	}
}