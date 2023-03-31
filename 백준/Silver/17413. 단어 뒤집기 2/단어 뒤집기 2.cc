#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;
#include <stack>

int main() {

    string str;
    getline(cin,str);
    stack<char> s;
    bool flag = true;
    for(int i=0;i<str.length();i++){
        if(str[i]==' '){
            while(!s.empty()){
                cout << s.top();
                s.pop();
            }
            cout << ' ';
        }
        else if(str[i]=='<'){
            while(!s.empty()){
                cout << s.top();
                s.pop();
            }
            flag = false;
            cout << '<';
        }
        else if(str[i]=='>'){
            flag=true;
            cout <<'>';
        }
        else if(!flag){
            cout << str[i];
        }
        else if(flag){
            s.push(str[i]);
        }
    }
    while(!s.empty()){
                cout << s.top();
                s.pop();
            }

}