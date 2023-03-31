#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;
#include <deque>

int main()
{

    int a, b;
    cin >> a >> b;
    deque<int> deque;
    for (int i = 1; i <= a; i++)
    {
        deque.push_back(i);
    }
    cout << '<';
    while (!deque.empty())
    {
        for (int i = 0; i < b - 1; i++)
        {
            deque.push_back(deque.front());
            deque.pop_front();
        }
        if (deque.size() == 1)
        {
            cout << deque.front();
        }
        else 
            cout << deque.front() << ", ";
        deque.pop_front();
    }
    cout << '>';
}