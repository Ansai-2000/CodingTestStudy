#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main() {
    vector<int> heights(9);
    int sum = 0;
    for(int i=0;i<9;i++){
        cin >> heights[i];
        sum += heights[i];
    }

    sort(heights.begin(), heights.end()); // 오름차순 정렬

    for(int i=0;i<9;i++){
        for(int j=i+1;j<9;j++){
            if(sum - heights[i] - heights[j] == 100){ // 일곱 난쟁이의 키의 합이 100인 경우
                for(int k=0;k<9;k++){
                    if(k == i || k == j) continue; // 건너뛰기
                    cout << heights[k] << '\n'; // 출력
                }
                return 0; // 프로그램 종료
            }
        }
    }
    return 0;
}
