#include <iostream>
#include <vector>
using namespace std;

int n;
vector<int> arr(1000001,0);
int main()
{

    arr[0]=arr[1]=-1;
    for (int i = 2; i*i <=1000000; i++)
    {
        for (int j = i * i; j < 1000000; j = j + i)
        {
            if(arr[j]==-1) continue;
            else arr[j] = -1;
        }
        
    }

    while (true)
    {
        scanf("%d",&n);
        if(n==0) break;
        bool flag = false;
        for (int i = n;  i >= n / 2; i--)
        {

            if (arr[i]>=0 && arr[n-i]>=0)
            {

                printf("%d = %d + %d\n",n,n-i,i);
                flag = true;
                break;
            }
        }
        if (!flag)
        {
            printf("Goldbach's conjecture is wrong.\n");
        }
    }
}
