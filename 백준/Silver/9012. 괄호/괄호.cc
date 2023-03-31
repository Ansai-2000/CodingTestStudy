#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;
#include <stack>

int main() {

    int t;
    cin >> t;
    while(t--){
        string str;
        cin >> str;
        stack<int> a;
        bool flag = true;
        for(int i=0;i<str.length();i++){
            if(str[i]=='('){
                a.push(str[i]);

            }
            else if(str[i]==')'){
                if(a.size()==0){
                    flag = false;
                    break;
                }
                a.pop();
            }
        }
        if(a.size()==0&&flag==true)
            cout << "YES\n";
        else cout <<"NO\n";
    }

}