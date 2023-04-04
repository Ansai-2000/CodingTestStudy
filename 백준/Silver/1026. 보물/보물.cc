#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;


int main() {

    int n;
    cin >> n;
    vector<int> vA;
    vector<int> vB;
    for(int i=0;i<n;i++){
        int a;
        cin >> a;
        vA.push_back(a);
    }
    for(int i=0;i<n;i++){
        int a;
        cin >> a;
        vB.push_back(a);
    }
    sort(vA.begin(),vA.end());
    sort(vB.rbegin(),vB.rend());
    int sum = 0;
    for(int i=0;i<n;i++){
        sum = sum + vA[i]*vB[i];
    }
    cout << sum << endl;
}