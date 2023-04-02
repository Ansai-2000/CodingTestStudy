#include<bits/stdc++.h>
using namespace std;


int main() {

    int A,B;
    cin >> A>>B;
    int m;
    cin >> m;
    long long sum=0;
    int arr[m];
    for(int i=0;i<m;i++){
        cin>>arr[i];
    }
    for(int i=0;i<m;i++){
        sum+=arr[m-i-1]*pow(A,i);
    }
    vector<int>v;
    while(sum>0){
        v.push_back(sum%B);
        sum = sum/B;
    }
    reverse(v.begin(),v.end());
    for(int i=0;i<v.size();i++){
        cout << v[i] << ' ';
    }
    

}