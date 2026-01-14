#include <bits/stdc++.h>
using namespace std;
using ll = long long;
using pii = pair<int, int>;

string A;
string str;

const int MX = 300005;

char lres[MX];
int lidx = 0;
char rres[MX];
int ridx = 0;

bool lchk() {
    if(lidx < A.length()) return false;

    for(int i = 0; i < A.length(); i++) {
        if(lres[lidx-A.length()+i] != A[i]) return false;
    }

    return true;
}

bool rchk() {
    if(ridx < A.length()) return false;

    for(int i = 0; i < A.length(); i++) {
        if(rres[ridx-i-1] != A[i]) return false;
    }

    return true;
}

int main() {
    ios_base::sync_with_stdio(false); cin.tie(NULL);

    cin >> A;
    cin >> str;

    int L = 0, R = str.length()-1;

    bool flag = true;

    while(L <= R) {
        if(flag) {
            lres[lidx++] = str[L++];

            if(lchk()) {
                lidx -= A.length();

                flag = !flag;
            }
        } else {
            rres[ridx++] = str[R--];

            if(rchk()) {
                ridx -= A.length();

                flag = !flag;
            }
        }
    }
    
    // for(int i = 0; i < lidx; i++) cout << lres[i]; cout << "\n";
    // for(int i = ridx-1; i >= 0; i--) cout << rres[i]; cout << "\n";


    for(int i = 1; i <= ridx; i++) {
        lres[lidx++] = rres[ridx-i];

        if(lchk()) lidx -= A.length();
    }

    for(int i = 0; i < lidx; i++) cout << lres[i];

    return 0;
}