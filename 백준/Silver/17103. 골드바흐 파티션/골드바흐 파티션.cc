#include<bits/stdc++.h>
using namespace std;


int main() {

    bool arr[1000001] = {};
    arr[0]=arr[1]=1;
    for(int i=2;i*i<=1000000;i++){
        for(int j=i+i;j<=1000000;j=j+i){
            if(arr[j]==1){
                continue;
            }
            else{
                arr[j]=1;
            }
        }
    }
    int t;
    cin>>t;
    while(t--){
        int n;
        cin >>n;
        int i=2;
        int count=0;
        while(i<=n/2){
            if(arr[n-i]==0&&arr[i]==0){
                count++;
                
            }
            i++;
        }
        cout << count << endl;
    }
}