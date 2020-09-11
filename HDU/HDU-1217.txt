#include <iostream>
#include <stdio.h>
#include <string.h>
#include <map>
using namespace std;
double dt[1000][1000];
int n,m;
void Flayd()
{
    for (int k=0;k<n;k++)
        for (int i=0;i<n;i++)
            for (int j=0;j<n;j++)
                if (dt[i][j]<dt[i][k]*dt[k][j])
                    dt[i][j]=dt[i][k]*dt[k][j];
}
int main()
{
    char c[101],a[101];
    double b;
    int temp=1,i;
    while (scanf("%d",&n),n!=0)
    {
        int sum=0;
        memset(dt,0,sizeof(dt));
        map<string,int>mp;
        mp.clear();
        for (i=0;i<n;i++)
        {
            scanf("%s",c);
            mp[c]=sum++;
        }
        scanf("%d",&m);
        for (i=0;i<m;i++)
        {
            scanf("%s%lf%s",a,&b,c);
            dt[mp[a]][mp[c]]=b;
        }
        Flayd();
        for (i=0;i<n;i++)
        {
            if (dt[i][i]>1)
                break;
        }
        if (i<n)
            printf("Case %d: Yes\n",temp++);
        else
            printf("Case %d: No\n",temp++);
    }
    return 0;
}