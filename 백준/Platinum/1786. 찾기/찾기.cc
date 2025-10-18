#include<bits/stdc++.h>
using namespace std;
vector<int> getFail(string &b) {
    int n = b.length();
    vector<int> fail(n);

    for (int i = 1, j = 0; i < n; i++) {
        while (j && b[i] != b[j]) j = fail[j-1];
        if (b[i] == b[j]) fail[i] = ++j;
    }

    return fail;
}

// KMP(a, b) : 문자열 a에서 문자열 b가 나오는 위치 반환
// KMP("AAABAA", "AA") = {0, 1, 4}
vector<int> KMP(string &a, string &b) {
    int n = a.length(); int m = b.length();
    vector<int> fail, ret; fail = getFail(b);

    for (int i = 0, j = 0; i < n; i++) {
        while (j && a[i] != b[j]) j = fail[j-1];
        if (a[i] == b[j]) {
            if (j + 1 == m) {
                ret.push_back(i - j + 1);
                j = fail[j];
            }
            else j++;
        }
    }

    return ret;
}
/*https://github.com/saywoo/competitive-programming-note/blob/main/source/string/kmp.cpp*/
int main(){
	string n;getline(cin,n);
	string m;getline(cin,m);
	auto i=KMP(n,m);
	cout << i.size() <<'\n';
	for (auto j:i){
		cout << j << ' ';
	}
	/*
	고마워요 세이우 역시 세우야 세우야 말로 우리 국민대의 영웅이지 
	*/
} 