#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main()
{

    int t;
    int a, b;
    cin >> t;
    int arr[100][100] = {};
    int count = 0;
    while (t--)
    {
        cin >> a >> b;
        for (int i = a; i < a + 10; i++)
        {
            for (int j = b; j < b + 10; j++)
            {

                if (arr[i][j] == 0)
                {
                    count++;
                    arr[i][j] = 1;
                }
            }
        }
    }
    cout << count;
}