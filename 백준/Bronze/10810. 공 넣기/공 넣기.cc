#include <iostream>
#include <string>
#include <cstring>
using namespace std;
int main(){
    int N,M;
    cin >> N >>M;
    int a[101];
    memset(a,0,sizeof(a));
    for(int m=0;m<M;m++){
        int i,j,k;
        cin >> i >> j >> k;
        for(int q=i;q<=j;q++){
            a[q] = k;
        }
    }
    for(int i=1;i<=N;i++){
        cout << a[i] << ' '; 
    }
}