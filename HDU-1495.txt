#include <iostream>
#include <stdio.h>
#include <string.h>
#include <queue>
using namespace std;
int S,M,N,temp[105][105][105];
struct node
{
    int x,y,z,pre;
};
bool place(int i,int j,int k)
{
    if ((j==k&&i==0)||(i==k&&j==0)||(i==j&&k==0))
        return true;
    return false;
}
int BFS(int x,int y,int z)
{
    queue<node>it;
    memset(temp,0,sizeof(temp));
    node o,e;
    e.x=x;
    e.y=0;
    e.z=0;
    e.pre=0;
    it.push(e);
    if (x%2!=0)
        return 0;
    temp[e.x][e.y][e.z]=1;
    while (!it.empty())
    {
        e=it.front();
        it.pop();
        int num;
        if (place(e.x,e.y,e.z))
        {
            printf("%d\n",e.pre);
            return 1;
        }
        if (e.x!=0)
        {
            if (e.y<y)
            {
                num=y-e.y;
                o.z=e.z;
                o.pre=e.pre+1;
                if (e.x>num)
                {
                    o.x=e.x-num;
                    o.y=y;
                }
                else
                {
                    o.x=0;
                    o.y=e.x+e.y;
                }
                if (!temp[o.x][o.y][o.z])
                {
                    temp[o.x][o.y][o.z]=1;
                    it.push(o);
                }
            }
            if (e.z<z)
            {
                num=z-e.z;
                o.y=e.y;
                o.pre=e.pre+1;
                if (e.x>num)
                {
                    o.x=e.x-num;
                    o.z=z;
                }
                else
                {
                    o.x=0;
                    o.z=e.x+e.z;
                }
                if (!temp[o.x][o.y][o.z])
                {
                    temp[o.x][o.y][o.z]=1;
                    it.push(o);
                }
            }
        }
        if (e.y>0)
        {
            if (e.x<x)
            {
                num=x-e.x;
                o.z=e.z;
                o.pre=e.pre+1;
                if (e.y>num)
                {
                    o.y=e.y-num;
                    o.x=x;
                }
                else
                {
                    o.y=0;
                    o.x=e.x+e.y;
                }
                if (!temp[o.x][o.y][o.z])
                {
                    temp[o.x][o.y][o.z]=1;
                    it.push(o);
                }
            }
            if (e.z<z)
            {
                num=z-e.z;
                o.x=e.x;
                o.pre=e.pre+1;
                if (e.y>num)
                {
                    o.y=e.y-num;
                    o.z=z;
                }
                else
                {
                    o.y=0;
                    o.z=e.y+e.z;
                }
                if (!temp[o.x][o.y][o.z])
                {
                    temp[o.x][o.y][o.z]=1;
                    it.push(o);
                }
            }
        }
        if (e.z>0)
        {
            if (e.y<y)
            {
                num=y-e.y;
                o.x=e.x;
                o.pre=e.pre+1;
                if (e.z>num)
                {
                    o.z=e.z-num;
                    o.y=y;
                }
                else
                {
                    o.z=0;
                    o.y=e.z+e.y;
                }
                if (!temp[o.x][o.y][o.z])
                {
                    temp[o.x][o.y][o.z]=1;
                    it.push(o);
                }
            }
            if (e.x<x)
            {
                num=x-e.x;
                o.y=e.y;
                o.pre=e.pre+1;
                if (e.z>num)
                {
                    o.z=e.z-num;
                    o.x=x;
                }
                else
                {
                    o.z=0;
                    o.x=e.x+e.z;
                }
                if (!temp[o.x][o.y][o.z])
                {
                    temp[o.x][o.y][o.z]=1;
                    it.push(o);
                }
            }
        }
    }
    return 0;
}
int main()
{
    while (scanf("%d %d %d",&S,&M,&N),S!=0||M!=0||N!=0)
    {
        int n=BFS(S,M,N);
        if (n==0)
            printf("NO\n");
    }
}