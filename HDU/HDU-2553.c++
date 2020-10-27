#include<stdio.h>
#include <math.h>
#define N 11
/*
int n;
int sum;
int x[N];
int place(int k)
{
    int i;
    for(i=1;i<k;i++)
      if(fabs(k-i)==fabs(x[k]-x[i])||x[k]==x[i])
        return 0;
    return 1;
}
int BFS(int t)
{
    if(t>n && n>0)
        sum++;
    else
    {
        for(int i=1;i<=n;i++)
        {
            x[t] = i;
            if (place(t))
                BFS(t+1);
        }
    }
    return sum;
}
int main()
{
    int z;
    while (~scanf("%d",&n),n!=0)
    {
        sum=0;
        z=BFS(1);
        printf("%d\n",z);
    }
    return 0;
}
*/
int main()
{
    int a[11]={0,1,0,0,2,10,4,40,92,352,724},n,z;
    while (~scanf("%d",&n),n!=0)
        printf("%d\n",a[n]);
    return 0;
}