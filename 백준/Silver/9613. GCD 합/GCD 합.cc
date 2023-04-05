#include<bits/stdc++.h>
using namespace std;

long long gcd(int a,int b){
    if(b==0) return a;
    return gcd(b,a%b);
}
int main() {

    int t;
    cin >> t;
    while(t--){
        int n;
        cin >> n;
        long long sum=0;
        int arr[101] = {};
        for(int i=0;i<n;i++){
            cin >> arr[i];
        }
        for(int i=0;i<n;i++){
            for(int j=i+1;j<n;j++){
                sum+=gcd(arr[i],arr[j]);
            }
        }
        cout << sum << endl;
    }

}