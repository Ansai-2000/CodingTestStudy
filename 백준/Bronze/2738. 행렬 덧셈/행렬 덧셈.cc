#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;


int main() {

    int a,b;
    cin >> a>>b;
    
    vector<int>vb[a];
    vector<int>va[a];
    vector<int>vc[a];
    int t;
    for(int i=0;i<a;i++){
        for(int j=0;j<b;j++){
            cin >> t;
            va[i].push_back(t);
        }
    }
    for(int i=0;i<a;i++){
        for(int j=0;j<b;j++){
            cin >> t;
            vb[i].push_back(t);
        }
    }
    for(int i=0;i<a;i++){
        for(int j=0;j<b;j++){
            cout << va[i][j]+vb[i][j] << ' ';
        }
        cout << endl;
    }
}