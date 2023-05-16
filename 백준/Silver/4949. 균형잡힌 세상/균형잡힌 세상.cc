#include<bits/stdc++.h>
using namespace std;


int main() {

    while (true)
    {
        
        string a;
        getline(cin,a);
        if(a==".")
            break;
        stack<char>s;
        bool inValid = true;
        for(auto c : a){
            if(c=='(' || c=='[')
                s.push(c);
            else if(c==')'){
                if(s.empty() || s.top() != '('){
                    inValid = false;
                    break;
                }
                s.pop();
            }
            else if(c==']'){
            if(s.empty() || s.top() != '['){
                inValid = false;
                break;
            }
            s.pop();
            }
        
        }
        if(!s.empty()) inValid = false;
        if(inValid) cout << "yes\n";
        else cout << "no\n";
        


    }
    

}