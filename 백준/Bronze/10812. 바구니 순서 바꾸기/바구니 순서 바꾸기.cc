#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;


int main() {

    int a,b;
    cin >> a>>b;
    int arr[101];
    for(int i=1;i<=100;i++){
        arr[i] = i;
    }
    int begin,mid,end;
    for(int i=0;i<b;i++){
        cin >> begin >> end >> mid;
        int start = begin;
        int brr[101]={0};
        for(int j=begin;j<mid;j++){
            brr[j] = arr[j];
        }
        for(int j=mid;j<=end;j++){
            arr[start] = arr[j];
            start++;
        }
        for(int j=begin;j<mid;j++){
            arr[start] = brr[j];
            start++;
        }
    }
    for(int i=1;i<=a;i++){
        cout << arr[i] << ' ';
    }
    

}