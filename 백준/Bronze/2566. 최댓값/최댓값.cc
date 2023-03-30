#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;


int main() {

    int max=0;
    int maxi;
    int maxj;
    int a;
    for(int i=1;i<=9;i++){
        for(int j=1;j<=9;j++){
            cin >> a;
            if(max<=a){
                max = a;
                maxi = i;
                maxj = j;
            }  
        }
    }
    cout << max << "\n" << maxi <<' '<<maxj;

}