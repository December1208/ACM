#include <iostream>
#include <stdio.h>
using namespace std;
int BFS(int t)
{
    if (t==0)
        return 1;
    if (t==1)
        return 3;
    return 2*BFS(t-1)+BFS(t-2);
}
int main()
{
    int t,num,n;
    scanf("%d",&num);
    while (num--)
    {
        scanf("%d",&n);
        t=BFS(n);
        printf("%d\n",t);
    }
    return 0;
}