#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

#include <map>
int main() {
    map<int,bool> map;
    int n,m;
    cin >> n>>m;
    int num;
    for(int i=0;i<n+m;i++){
        cin >> num;
        if(map[num]==true)
            map.erase(num);
        else
        map[num] = true;
    }
    cout << map.size();

}