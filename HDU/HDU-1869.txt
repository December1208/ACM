#include <iostream>
#include <string.h>
#include <stdio.h>
#define INF 0x3f3f3f
using namespace std;
int m,n,chara[101][101];
void Floyd()
{
    for (int k=0;k<m;k++)
    {
        for (int i=0;i<m;i++)
        {
            for (int j=0;j<m;j++)
                if (chara[i][j]>chara[i][k]+chara[k][j])
                    chara[i][j]=chara[i][k]+chara[k][j];
        }
    }
}
int main()
{
    int a,b,i,j;
    while (~scanf("%d %d",&m,&n))
    {
        memset(chara,0x3f,sizeof(chara));
        for (int i=0;i<n;i++)
        {
            scanf("%d %d",&a,&b);
            chara[a][b]=chara[b][a]=1;
        }
        Floyd();
        for (i=0;i<m;i++)
        {
            for (j=0;j<m;j++)
                if (chara[i][j]>7)
                {
                    printf("No\n");
                    break;
                }
            if (j<m)
                break;
        }
        if (i==m)
            printf("Yes\n");
    }
    return 0;
}