/*
virtual contest
그게왜진조잘못이느냐: kangsm02, Yoisaki-Kanade, saywoo
*/

#include <bits/stdc++.h>
using namespace std;

using ll = long long int;

const int MX = 105;

int mat[MX][MX];

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    int tc; cin >> tc;
    while(tc--) {
        int n;
        cin >> n;

        for(int i = 0; i < n; i++) {
            for(int j = 0; j < n; j++) {
                cin >> mat[i][j];
            }
        }
        
        multiset<int> row[MX];
        multiset<int> col[MX];

        vector<int> ndr;
        vector<int> ndc;

        for(int i = 0; i < n; i++) {
            set<int> dupe;

            for(int j = 0; j < n; j++) {
                row[i].insert(mat[i][j]);
                dupe.insert(mat[i][j]);
            }

            if(dupe.size()==n) ndr.push_back(i);
        }
        
        
        for(int j = 0; j < n; j++) {
            set<int> dupe;

            for(int i = 0; i < n; i++) {
                col[j].insert(mat[i][j]);
                dupe.insert(mat[i][j]);
            }

            if(dupe.size()==n) ndc.push_back(j);
        }

        
        cout << max(ndr.size(), ndc.size()) << '\n';
        int i = 0;
        for(; i < min(ndr.size(), ndc.size()); i++) {
            cout << ndr[i]+1 << " " << ndc[i]+1 << " ";

            if(mat[ndr[i]][ndc[i]] == 1) {
                row[ndr[i]].erase(1);
                col[ndc[i]].erase(1);

                row[ndr[i]].insert(2);
                col[ndc[i]].insert(2);
            
                mat[ndr[i]][ndc[i]] = 2;
            } else {
                row[ndr[i]].erase(mat[ndr[i]][ndc[i]]);
                col[ndc[i]].erase(mat[ndr[i]][ndc[i]]);

                row[ndr[i]].insert(1);
                col[ndc[i]].insert(1);

                mat[ndr[i]][ndc[i]] = 1;
            }

            cout << mat[ndr[i]][ndc[i]] << "\n";
        }

        // cout << ndr.size() << " " << ndc.size() << "\n\n\n";

        for(; i < ndr.size(); i++) {
            bool flag = false;
            int r=ndr[i];
            
            for(int j = 0; j < n && !flag; j++) {
                for(int cnt = 1; cnt <= n; cnt++) {
                    if(mat[r][j] == cnt) continue;

                    vector<int> freq(n+1);
                    
                    for (int ii=0;ii<n;ii++) freq[mat[ii][j]]++;
                    
                    freq[mat[r][j]]--;
                    freq[cnt]++;
                    
                    bool ist=0;
                    for (int x=1;x<=n;x++){
                    	if (freq[x]>=2){
                    		ist=1;
                    		break;
						}
					}
		            if (!ist)continue;
		            
		            cout << r+1 << ' ' << j+1 << ' ' << cnt << '\n';
		            mat[r][j]=cnt;
		            flag = true;
		            break;
                }
            }

            // if(!flag) exit(-1);
        }

        for(; i < ndc.size(); i++) {
            bool flag = false;
            int c=ndc[i];
            for(int j = 0; j < n && !flag; j++) {

                for(int cnt = 1; cnt <= n; cnt++) {
                    if(mat[j][c] == cnt) continue;

                    vector<int> freq(n+1);
                    
                    for (int ii=0;ii<n;ii++) freq[mat[j][ii]]++;
                    
                    freq[mat[j][c]]--;
                    freq[cnt]++;
                    
                    bool ist=0;
                    
                    for (int x=1;x<=n;x++){
                    	if (freq[x]>=2){
                    		ist=1;
                    		break;
						}
					}
					if (!ist) continue;
					
					cout << j+1 << ' ' << c+1 << ' ' << cnt << '\n';
					mat[j][c]=cnt;
					flag=true;
					break;
                }
			}
            // if(!flag) exit(-1);
        }

    }

    
    return 0;
}
