#include<bits/stdc++.h>
using namespace std;
main(){
	cin.tie(0);
	ios::sync_with_stdio(false);
	int a;
	cin >>a;
	cout <<"int a;";
	for (int i=1;i<=a;i++){
		cout<<"\nint ";
		for (int j=0;j<i;j++){
			cout<<"*";
		}
		cout <<"ptr";
		if (i==1){
			cout<<" = &a;";
		}
		else if (i==2){
			cout<< i <<" = &ptr;";
		}
		else{
			cout<< i <<" = &ptr"<<i-1<<";";
		}
	}
}