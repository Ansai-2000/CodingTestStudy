#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;


int main() {

    int n;
    cin >> n;
    vector<int> v;
    for(int i=0;i<n;i++){
        int a;
        cin >> a;
        v.push_back(a);
    }
    sort(v.begin(),v.end());
    int s = v[0];
    cout << s << ' ';
    for(int i=1;i<v.size();i++){
        if(s!=v[i]){
            s = v[i];
            cout << s << ' ';
        }
    }

}