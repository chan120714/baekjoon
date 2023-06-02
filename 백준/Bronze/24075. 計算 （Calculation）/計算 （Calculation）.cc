#include<bits/stdc++.h>
using namespace std;
main(){
    cin.tie(0);
    ios::sync_with_stdio(false);
    int a,b,c,d;
    cin >>a>>b;
    c=a+b;d=a-b;
    if (c>=d){
        cout<<c<<"\n"<<d;
    }
    else{
        cout << d <<"\n" << c;
    }
}