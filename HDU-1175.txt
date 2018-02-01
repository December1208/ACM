#include <iostream>
#include <stdio.h>
#include <string.h>
#include <queue>
using namespace std;
struct node
{
    int x,y,pre;
};
int dt[1005][1005],h,l;
int xy[4][2]={0,1,0,-1,1,0,-1,0},temp[1005][1005];
void BFS(int xt,int yt,int xl,int yl)
{
    queue<node>it;
    memset(temp,0,sizeof(temp));
    if (dt[xt][yt]==0||dt[xl][yl]==0)
    {
        printf("NO\n");
        return ;
    }
    else if (xt==xl&&yt==yl)
    {
        printf("NO\n");
        return ;
    }
    else if (dt[xt][yt]!=dt[xl][yl])
    {
        printf("NO\n");
        return ;
    }
    node o,e;
    e.x=xt;
    e.y=yt;
    e.pre=0;
    it.push(e);
    temp[e.x][e.y]=1;
    while (!it.empty())
    {
        e=it.front();
        it.pop();
        for (int i=0;i<4;i++)
        {
            o.x=e.x+xy[i][0];
            o.y=e.y+xy[i][1];
            o.pre=e.pre;
            while (1)
            {
                if (temp[o.x][o.y]||o.pre>=3||dt[o.x][o.y]!=0||o.x<1||o.x>h||o.y<1||o.y>l)
                    break;
                temp[o.x][o.y]=1;
                o.pre+=1;
                it.push(o);
                o.pre-=1;
                o.x+=xy[i][0];
                o.y+=xy[i][1];
            }
            if (o.x==xl&&o.y==yl&&o.pre<3)
            {
                printf("YES\n");
                return ;
            }
        }
    }
    printf("NO\n");
}
int main()
{
    int n,xq,yq,xz,yz;
    while (~scanf("%d %d",&h,&l),h!=0||l!=0)
    {
        for (int i=1;i<=h;i++)
            for (int j=1;j<=l;j++)
                scanf("%d",&dt[i][j]);
        scanf("%d",&n);
        while (n--)
        {
            scanf("%d %d %d %d",&xq,&yq,&xz,&yz);
            BFS(xq,yq,xz,yz);
        }
       // memset(dt,0,sizeof(dt));
    }
    return 0;
}