#include <iostream>
#include <stdio.h>
#include <string.h>
#include <queue>
using namespace std;
int m,n,temp[100001];
struct node
{
    int i,pre;
};
int BFS(int x,int y)
{
    queue<node>it;
    memset(temp,0,sizeof(temp));
    node o,e;
    e.i=x;
    e.pre=0;
    temp[e.i]=1;
    it.push(e);
    if (x==y)
        return 0;
    while (!it.empty())
    {
        e=it.front();
        it.pop();
        for (int i=0;i<3;i++)
        {
            if (i==0)
                o.i=e.i+1;
            if (i==1)
                o.i=e.i-1;
            if (i==2)
                o.i=e.i*2;
            o.pre=e.pre+1;
            if (o.i==y)
                return o.pre;
            if (o.i<0||o.i>100000||temp[o.i])
                continue;
            temp[o.i]=1;
            it.push(o);
        }
    }
}
int main()
{
    while (~scanf("%d %d",&m,&n))
    {
        printf("%d\n",BFS(m,n));
    }
    return 0;
}