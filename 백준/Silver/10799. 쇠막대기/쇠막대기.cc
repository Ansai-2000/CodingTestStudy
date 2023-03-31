#include<bits/stdc++.h>
using namespace std;

int main() {

    string str;
    cin >> str;
    int count=0;
    stack<char> s;
    for(int i=0;i<str.length();i++){
        if(str[i]=='('){
            s.push(str[i]);
        }
        else{
            s.pop();
            if(str[i-1]=='('){
                count+=s.size();
            }
            else{
                count ++;
            }
        }
    }
    cout << count;

}