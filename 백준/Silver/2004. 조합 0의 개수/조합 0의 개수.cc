#include<bits/stdc++.h>
using namespace std;

long long func(long a,int b){

    int count=0;
    for(long long i=b;a/i>=1;i*=b){
        count += a/i;
    }
    
    return count;
}
int main() {

    long n,m;
    cin >> n>>m;
    long long two = func(n,2)-func(n-m,2)-func(m,2);
    long long five = func(n,5)-func(n-m,5)-func(m,5);
    cout << min(two,five);

}