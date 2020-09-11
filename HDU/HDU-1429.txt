#include <iostream>
#include <stdio.h>
#include <string.h>
#include <queue>
using namespace std;
struct node
{
    int x,y,key,pre;
};
char dt[21][21];
int bu,m,n,temp[21][21][1025],xy[4][2]={0,1,0,-1,1,0,-1,0};
int place(int x,int y,int k,int b)
{
    if (temp[x][y][k]||dt[x][y]=='*'||x<0||x>=m||y<0||y>=n||b>=bu)
        return 1;
    return 0;
}
int BFS(int xt,int yt)
{
    queue<node>it;
    memset(temp,0,sizeof(temp));
    node o,e;
    e.x=xt;
    e.y=yt;
    e.pre=0;
    e.key=0;
    it.push(e);
    temp[e.x][e.y][e.key]=1;
    while (!it.empty())
    {
        e=it.front();
        it.pop();
        for (int l=0;l<4;l++)
        {
            o.x=e.x+xy[l][0];
            o.y=e.y+xy[l][1];
            o.key=e.key;
            o.pre=e.pre+1;
            if (place(o.x,o.y,o.key,o.pre))
                continue;
            else if (dt[o.x][o.y]=='^')
                return o.pre;
            else if (dt[o.x][o.y]>='a'&&dt[o.x][o.y]<='j')
            {
                int stc=dt[o.x][o.y]-'a';
                if ((o.key&(1<<stc))==0)
                    o.key+=(1<<stc);
            }
            else if (dt[o.x][o.y]>='A'&&dt[o.x][o.y]<='J')
            {
                int stc=dt[o.x][o.y]-'A';
                if ((o.key&(1<<stc))==0)
                    continue;
            }
            it.push(o);
            temp[o.x][o.y][o.key]=1;
        }
    }
    return -1;
}
int main()
{
    int d,s,r;
    while (~scanf("%d %d %d",&m,&n,&bu))
    {
        for (int i=0;i<m;i++)
        {
            getchar();
            for (int j=0;j<n;j++)
            {
                scanf("%c",&dt[i][j]);
                if (dt[i][j]=='@')
                {
                    s=i;r=j;
                }
            }
        }
        d=BFS(s,r);
        printf("%d\n",d);
        getchar();
    }
    return 0;
}