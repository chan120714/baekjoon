#include<bits/stdc++.h>
typedef int A;
int main(){
	A*Lixx;
	A*saywoo;
	int n,m;std::cin >> n >> m;
	Lixx=&n;
	saywoo=&m;
    int Credits=*Lixx+*saywoo;
	std::cout << Credits;
}