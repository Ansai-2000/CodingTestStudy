#include <bits/stdc++.h>
using namespace std;

int arr[1000001];
    int brr[1000001];
    int n;
int main()
{

    
    cin >> n;
    for(int i=0;i<n;i++){
        cin >> arr[i];
    }
    stack<int> s;
    for (int i = n-1; i >=0; i--)
    {
        while(!s.empty()&&s.top()<=arr[i]){
            s.pop();
        }
        if(s.empty()) brr[i] = -1;
        else brr[i] = s.top();
        s.push(arr[i]);
    }
    for(int i=0;i<n;i++){
        cout << brr[i] << ' ';
    }
}