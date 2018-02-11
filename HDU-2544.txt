#include <iostream>
#include <stdio.h>
#include <string.h>
#define INF 0x3f3f3f3f
using namespace std;
int chara[101][101],M,N;
void Floyd()
{
    for (int k=1;k<=N;k++)
    {
        for (int i=1;i<=N;i++)
        {
            for (int j=1;j<=N;j++)
            {
                if (chara[i][j]>chara[i][k]+chara[k][j])
                    chara[i][j]=chara[i][k]+chara[k][j];
            }
        }
    }
}
int main()
{
    int a,b,c;
    while (scanf("%d %d",&N,&M),N!=0||M!=0)
    {
        memset(chara,0x3f,sizeof(chara));
        for (int i=0;i<M;i++)
        {
            scanf("%d %d %d",&a,&b,&c);
            chara[a][b]=chara[b][a]=c;
        }
        Floyd();
        printf("%d\n",chara[1][N]);
    }
    return 0;
}