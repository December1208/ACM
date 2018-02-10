#include <iostream>
#include <stdio.h>
#include <string.h>
#include <map>
#define INF 0x3f3f3f3f
using namespace std;
int chara[155][155];
int ans,dis[155],vis[155];
void Dijkstra(int str)
{
    memset(dis,0x3f,sizeof(dis));
    memset(vis,0,sizeof(vis));
    for (int i=1;i<ans;i++)
        dis[i]=chara[str][i];
    dis[str]=0;
    vis[str]=1;
    for (int i=1;i<ans;i++)
    {
        int stc=INF,k;
        for (int j=1;j<ans;j++)
        {
            if (!vis[j]&&dis[j]<stc)
            {
                stc=dis[j];
                k=j;
            }
        }
        if (stc==INF)
            break;
        vis[k]=1;
        for (int j=1;j<ans;j++)
            if (!vis[j]&&dis[j]>dis[k]+chara[k][j])
                dis[j]=dis[k]+chara[k][j];
    }
}
int main()
{
    int n,time,k;
    char a[30],b[30];
    map<string,int>mp;
    char start[31],ends[31];
    while (scanf("%d",&n)&&n!=-1)
    {
        k=0;
        mp.clear();
        scanf("%s%s",start,ends);
        if (strcmp(start,ends)==0)
            k=1;
        mp[start]=1;
        mp[ends]=2;
        memset(chara,0x3f,sizeof(chara));
        ans=3;
        for (int i=1;i<=155;i++)
            chara[i][i]=0;
        for (int i=0;i<n;i++)
        {
            scanf("%s%s%d",a,b,&time);
            if (!mp[a])
                mp[a]=ans++;
            if (!mp[b])
                mp[b]=ans++;
            if (time<chara[mp[a]][mp[b]])
                chara[mp[a]][mp[b]]=chara[mp[b]][mp[a]]=time;
        }
        if (k==1)
            printf("0\n");
        else
        {
            Dijkstra(1);
            if (dis[2]<INF)
                printf("%d\n",dis[2]);
            else
                printf("-1\n");
        }
    }
    return 0;
}