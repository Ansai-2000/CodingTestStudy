#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;
#include <stack>
#include <string>

int main()
{

    int n;
    cin >> n;

    stack<int> st;
    string str;
    while (n--)
    {
        cin >> str;
        if (str == "push")
        {
            int num;
            cin >> num;
            st.push(num);
        }
        else if (str == "pop")
        {
            if (!st.empty())
            {
                cout << st.top() << endl;
                st.pop();
            }
            else
            {
                cout << "-1" << endl;
            }
        }
        else if (str == "empty")
        {
            if (st.empty())
            {
                cout << "1" << endl;
            }
            else
            {
                cout << "0" << endl;
            }
        }
        else if (str == "size")
        {
            cout << st.size() << endl;
        }
        else if (str == "top")
        {
            if (!st.empty())
            {
                cout << st.top() << endl;
            }
            else
            {
                cout << "-1" << endl;
            }
        }
    }
}
