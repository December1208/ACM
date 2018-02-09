#include <iostream>
#include <stdio.h>
#include <string.h>
#define INF 0x3f3f3f3f
using namespace std;
int T,S,D,chara[1010][1010],m[1010],n[1010],vis[1010],dis[1010],sum;
int Min(int a,int b)
{
    return a<b?a:b;
}
int Max(int a,int b)
{
    return a>b?a:b;
}
void Dijkstra(int str)
{
    for (int k=1;k<=sum;k++)
    {
        dis[k]=chara[str][k];
        vis[k]=0;
    }
    dis[str]=0;
    vis[str]=1;
    for (int k=1;k<=sum;k++)
    {
        int stc=INF,t;
        for (int l=1;l<=sum;l++)
        {
            if (!vis[l]&&stc>dis[l])
            {
                t=l;
                stc=dis[l];
            }
        }
        if (stc==INF)
            break;
        vis[t]=1;
        for (int l=1;l<=sum;l++)
            if (!vis[l])
                dis[l]=Min(dis[l],dis[t]+chara[t][l]);
    }
}
int main()
{
    int a,b,time;
    while (~scanf("%d %d %d",&T,&S,&D))
    {
        memset(chara,0x3f,sizeof(chara));
        sum=0;
        for (int i=0;i<T;i++)
        {
            scanf("%d %d %d",&a,&b,&time);
            if (time<chara[a][b])
                chara[a][b]=chara[b][a]=time;
            sum=Max(Max(a,b),sum);
        }
        for (int i=0;i<S;i++)
            scanf("%d",&m[i]);
        for (int i=0;i<D;i++)
            scanf("%d",&n[i]);
        int ans=INF;
        for (int i=0;i<S;i++)
        {
            Dijkstra(m[i]);
            for (int j=0;j<D;j++)
                ans=Min(ans,dis[n[j]]);
        }
        printf("%d\n",ans);
    }
    return 0;
}