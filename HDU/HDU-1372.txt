#include <iostream>
#include <stdio.h>
#include <string.h>
#include <queue>
using namespace std;
char dt[200][200];
int h1,h2,m,n,xl,xt,yl,yt;
char l1,l2;
int xy[8][2]={1,-2,2,-1,1,2,2,1,-1,2,-2,1,-1,-2,-2,-1},temp[200][200];
struct cmp
{
    int i,j,pre;
    friend bool operator < (cmp a,cmp b)
    {
        return a.pre>b.pre;
    }
};
priority_queue<cmp>it;
int BFS(int x,int y)
{
    memset(temp,0,sizeof(temp));
    cmp e,o;
    e.i=x;
    e.j=y;
    e.pre=0;
    it.push(e);
    temp[e.i][e.j]=1;
    while (!it.empty())
    {
        e=it.top();
        it.pop();
        if (e.i==n&&e.j==h2)
        {
            return e.pre;
        }
        for (int t=0;t<8;t++)
        {
            o=e;
            o.i+=xy[t][0];
            o.j+=xy[t][1];
            if (o.i>8||o.j>8||o.i<=0||o.j<=0||temp[o.i][o.j])
                continue;
            o.pre++;
            temp[o.i][o.j]=1;
            it.push(o);
        }
    }
    return 0;
}
int main()
{

    while (~scanf("%c%d %c%d",&l1,&h1,&l2,&h2))
    {
        while (!it.empty())
        {
            it.pop();
        }
        getchar();
        m=l1-96;
        n=l2-96;
        int num=BFS(m,h1);
        printf("To get from %c%d to %c%d takes %d knight moves.\n",l1,h1,l2,h2,num);
    }
    return 0;
}