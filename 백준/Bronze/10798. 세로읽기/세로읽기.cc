#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;


int main() {

    string str;
    char c[5][15] = {};
    for(int i=0;i<5;i++){
        cin >> str;
        for(int j=0;j<str.length();j++){
            c[i][j] = str[j];
        }
    }
    for(int i=0;i<15;i++){
        for(int j=0;j<5;j++){
            if(c[j][i]==char(0)){
                continue;
            }
            cout << c[j][i];
        }
    }

}