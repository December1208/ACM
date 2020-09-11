#include <iostream>
#include <stdio.h>
#include <queue>
#include <string.h>
using namespace std;
int dt[55][55][55],xyz[6][3]={1,0,0,-1,0,0,0,-1,0,0,1,0,0,0,1,0,0,-1},temp[55][55][55],x,y,z,te;
struct cmp
{
    int i,j,z,pre;
    friend bool operator < (cmp a,cmp b)
    {
        return a.pre>b.pre;
    }
};
priority_queue<cmp>it;
int BFS()
{
    memset(temp,0,sizeof(temp));
    cmp e,o;
    e.i=0;
    e.j=0;
    e.z=0;
    e.pre=0;
    it.push(e);
    temp[e.i][e.j][e.z]=1;
    if (x+y+z-3>te)
        return -1;
    while (!it.empty())
    {
        e=it.top();
        it.pop();
        for (int t=0;t<6;t++)
        {
            o=e;
            o.i+=xyz[t][0];
            o.j+=xyz[t][1];
            o.z+=xyz[t][2];
            if (dt[o.i][o.j][o.z]==1||temp[o.i][o.j][o.z]==1||o.i>=x||o.j>=y||o.z>=z||o.i<0||o.j<0||o.z<0)
                continue;
            o.pre++;
            if (o.i==x-1&&o.j==y-1&&o.z==z-1)
            {
                return o.pre;
            }
            if (x+y+z+o.pre-o.i-o.j-o.z-3>te)
                continue;
            temp[o.i][o.j][o.z]=1;
            it.push(o);
        }
    }
    return -1;
}
int main()
{
    int n;
    scanf("%d",&n);
    for (int h=0;h<n;h++)
    {
        while (!it.empty())
        {
            it.pop();
        }
        scanf("%d %d %d %d",&x,&y,&z,&te);
        for (int j=0;j<x;j++)
            for (int k=0;k<y;k++)
                for (int l=0;l<z;l++)
                    scanf("%d",&dt[j][k][l]);
        int num=BFS();
        printf("%d\n",num);
    }
    return 0;
}