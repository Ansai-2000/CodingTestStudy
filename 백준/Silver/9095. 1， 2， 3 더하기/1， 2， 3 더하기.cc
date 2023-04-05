#include<bits/stdc++.h>
using namespace std;


int main() {

    int dp[11]={};
    int t;
    cin >> t;
    dp[1]=1;
    dp[2]=2;
    dp[3]=4;
    for(int i=4;i<=10;i++){
        dp[i]=dp[i-1]+dp[i-2]+dp[i-3];
    }
    while(t--){
        int a;
        cin >> a;
        cout << dp[a] << endl;
    }

}