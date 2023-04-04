#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;
#include <deque>

int main()
{

    int n;
    cin >> n;
    string command;
    int command_num;
    deque<int> deque;
    for (int i = 0; i < n; i++)
    {
        cin >> command;

        if (command == "push_front")
        {
            cin >> command_num;
            deque.push_front(command_num);
        }
        else if (command == "push_back")
        {
            cin >> command_num;
            deque.push_back(command_num);
        }
        else if (command == "size")
        {
            cout << deque.size() << endl;
        }
        else if (command == "empty")
        {
            cout << deque.empty() << endl;
        }
        else if (deque.empty())
        {
            cout << -1 << endl;
        }
        else if (command == "pop_front")
        {
            cout << deque.front() << endl;
            deque.pop_front();
        }
        else if (command == "pop_back")
        {
            cout << deque.back() << endl;
            deque.pop_back();
        }
        else if (command == "front")
        {
            cout << deque.front() << endl;
        }
        else if (command == "back")
        {
            cout << deque.back() << endl;
        }
    }
}