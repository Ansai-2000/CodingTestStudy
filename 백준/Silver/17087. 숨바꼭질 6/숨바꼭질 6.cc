#include<bits/stdc++.h>
using namespace std;

long long gcd(long long a, long long b){
    if(b==0) return a;
    return gcd(b,a%b);
}
int main() {

   long long n;
   long long s;
   cin >> n >> s;
   long long a;
   long long t;
   vector<long long> v;
   while(n--){
    cin >> a;
    v.push_back(abs(s-a));
   } 
   
   t = gcd(v[0],v[1]);
   for(int i=0;i<v.size();i++){
    t = gcd(t,v[i]);
   }
    cout << t;
}