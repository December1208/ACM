#include <iostream>
#include <stdio.h>
#include <string.h>
#include <queue>
using namespace std;
char words[10001][10001];
int temp[10001],n;
int BFS()
{
    int a,k;
    queue<int>it;
    memset(temp,0,sizeof(temp));
    for (int i=0;i<n;i++)
    {
        if (words[i][0]=='b')
        {
           it.push(i);
           temp[i]=1;
        }
    }
    while (!it.empty())
    {
        a=it.front();
        it.pop();
        k=strlen(words[a]);
        for (int j=0;j<n;j++)
        {
            if (words[a][k-1]=='m')
            {
                return 1;
            }
            if (!temp[j]&&words[a][k-1]==words[j][0])
            {
                it.push(j);
                temp[j]=1;
            }
        }
    }
    return 0;
}
int main()
{
    int flag;
    while (~scanf("%s",words[0]))
    {
        for (int i=1;;i++)
        {
            gets(words[i]);
            if (words[i][0]=='0')
            {
                n=i;
                break;
            }
        }
        flag=BFS();
        if (flag==1)
            printf("Yes.\n");
        else
            printf("No.\n");
    }
    return 0;
}
