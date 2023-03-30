#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;


int main() {

    int a = 2;
    int n;
    cin >> n;
    int sum;
    for(int i=0;i<n;i++){
        a+=a-1;
    }
    sum = a*a;
    cout << sum;

}