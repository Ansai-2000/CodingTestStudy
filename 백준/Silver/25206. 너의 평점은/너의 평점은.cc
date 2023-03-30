#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;


int main() {

    string str;
    double a;
    string b;
    double sum = 0;
    double c = 0;
    for(int i=0;i<20;i++){
        cin >> str >> a>>b;
        
        if(b=="P"){
            continue;
        }
        else{
            if(b=="A+"){
                sum+=a*4.5;
            }
            else if(b=="A0"){
                sum+=a*4;
            }
            else if(b=="B+"){
                sum+=a*3.5;
            }
            else if(b=="B0"){
                sum+=a*3.0;
            }
            else if(b=="C+"){
                sum+=a*2.5;
            }

            else if(b=="C0"){
                sum+=a*2.0;
            }
            else if(b=="D+"){
                sum+=a*1.5;
            }
            else if(b=="D0"){
                sum+=a*1.0;
            }
            else if(b=="F"){
                sum+=0;
            }
        }
        c+=a;
    }
    cout << sum/c;

}