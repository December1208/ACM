#include <iostream>
#include <stdio.h>
using namespace std;
int xy[4][2]={1,0,0,-1,0,1,-1,0};
char dt[20][20];
int num;
int m,n;
void DFS(int x,int y)
{
    int X,Y;
    if (dt[x][y]!='.'||x>=n||y>=m||x<0||y<0)
        return;
    dt[x][y]='#';
    num++;
    for(int i=0;i<4;i++)
    {
        X=x+xy[i][0];
        Y=y+xy[i][1];
        DFS(X,Y);
    }
}
int main()
{
    while (~scanf("%d %d",&m,&n),m!=0&&n!=0)
    {
        num=0;
        for (int i=0;i<n;i++)
            for (int j=0;j<m;j++)
               cin>>dt[i][j];
        for (int i=0;i<n;i++)
        {
            for (int j=0;j<m;j++)
                if (dt[i][j]=='@')
                {
                    dt[i][j]='.';
                    DFS(i,j);
                }
        }
        cout<<num<<endl;
    }
    return 0;
}
