#include<bits/stdc++.h>
using namespace std;


int main() {

    int dp[301][3];
    int t;
    cin >> t;
    int arr[t+1] = {};
    for(int i=1;i<=t;i++){
        cin >> arr[i];
    }
    if(t==1){
        cout << arr[1];
        return 0;
    }
    dp[1][1] = arr[1];
    dp[1][2] = 0;
    dp[2][1] = arr[2];
    dp[2][2] = arr[1]+arr[2];
    for(int i=3;i<=t;i++){
        dp[i][1] = max(dp[i-2][1],dp[i-2][2])+arr[i];
        dp[i][2] = dp[i-1][1]+arr[i];
    }
    cout << max(dp[t][1],dp[t][2]);

}