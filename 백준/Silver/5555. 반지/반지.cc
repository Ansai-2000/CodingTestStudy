#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;


int main() {

    string str;
    cin >> str;
    int n;
    cin >> n;
    int count = 0;
    while(n--){
        string a;
        cin >> a;
        a+=a;
        if(a.find(str)!=string::npos){
            count++;
        }
    }
    cout << count;
}