#include<bits/stdc++.h>
using namespace std;

int arr[1000001]={};
    int brr[1000001]={};
    int n;
int main() {

    
    cin >> n;
    int A[n] = {};
    stack<int> s;
    for(int i=1;i<=n;i++){
        int a;
        cin >> a;
        arr[a]++;
        A[i] = a;
    }
    for(int i=n;i>0;i--){
        while(!s.empty()&&arr[A[i]]>=arr[s.top()]){
            s.pop();
        }
        if(s.empty()) brr[i]=-1;
        else brr[i] = s.top();
        s.push(A[i]);

    }

    for(int i=1;i<=n;i++){
        cout << brr[i] << ' ';
    }
}
