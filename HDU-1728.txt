#include <iostream>
#include <stdio.h>
#include <string.h>
#include <queue>
using namespace std;
struct node
{
    int x,y,pre;
};
char dt[105][105];
int xy[4][2]={0,1,0,-1,1,0,-1,0},temp[105][105],h,l;
void BFS(int xt,int yt,int xl,int yl,int zg)
{
    queue<node>it;
    memset(temp,0,sizeof(temp));
    node o,e;
    if (xt==xl&&yt==yl)
    {
        printf("yes\n");
        return ;
    }
    e.x=xt;
    e.y=yt;
    e.pre=-1;
    it.push(e);
    temp[e.x][e.y]=1;
    while (!it.empty())
    {
        e=it.front();
        if (e.pre>=zg)
            break;
        it.pop();
        for (int i=0;i<4;i++)
        {
            o.x=e.x+xy[i][0];
            o.y=e.y+xy[i][1];
            o.pre=e.pre+1;
            while (1)
            {
                if (dt[o.x][o.y]=='.'&&o.x>=1&&o.x<=h&&o.y>=1&&o.y<=l)
                {
                     if (o.x==xl&&o.y==yl)
                    {
                        printf("yes\n");
                        return ;
                    }
                    if (temp[o.x][o.y]==0)
                    {
                        temp[o.x][o.y]=1;
                        it.push(o);
                    }
                    o.x+=xy[i][0];
                    o.y+=xy[i][1];
                }
                else
                    break;
            }
        }
    }
    printf("no\n");
}
int main()
{
    int n,xq,yq,xz,yz,zhuan;
    scanf("%d",&n);
    while (n--)
    {
        scanf("%d %d",&h,&l);
        for (int i=1;i<=h;i++)
        {
            getchar();
            for (int j=1;j<=l;j++)
                scanf("%c",&dt[i][j]);
        }
        scanf("%d %d %d %d %d",&zhuan,&xq,&yq,&xz,&yz);
        BFS(yq,xq,yz,xz,zhuan);
    }
    return 0;
}