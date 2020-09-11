#include <iostream>
#include <stdio.h>
#include <string.h>
#include <queue>
using namespace std;
struct node
{
	int x, y, pre;
	friend bool operator < (node a, node b)
	{
		return a.pre>b.pre;
	}
};
char dt[22][22];
int temp[22][22], t, xy[4][2] = { 0,1,1,0,0,-1,-1,0 }, m, n;
int place(int xt, int yt)
{
	if (xt<0 || xt >= m || yt<0 || yt >= n || dt[xt][yt] == '*')
		return 1;
	return 0;
}
int direction(node now, node next)
{
	int pre;
	if (dt[next.x][next.y] == '|')
		pre = 1;
	else
		pre = 0;
	pre += now.pre % 2;
	return pre % 2;
}
int BFS(int x, int y)
{
	priority_queue<node>it;
	memset(temp, 0, sizeof(temp));
	node o, e;
	e.x = x;
	e.y = y;
	e.pre = 0;
	temp[e.x][e.y] = 1;
	it.push(e);
	while (!it.empty())
	{
		e = it.top();
		it.pop();
		if (dt[e.x][e.y] == 'T')
			return e.pre;
		for (int i = 0; i<4; i++)
		{
			o.x = e.x + xy[i][0];
			o.y = e.y + xy[i][1];
			o.pre = e.pre + 1;
			if (place(o.x, o.y) || temp[o.x][o.y])
				continue;
			else if (dt[o.x][o.y] == '.' || dt[o.x][o.y] == 'T')
			{
				temp[o.x][o.y] = 1;
				it.push(o);
				continue;
			}
			else
			{
				if (direction(e, o) != (i % 2))
					o.pre++;
				o.x += xy[i][0];
				o.y += xy[i][1];
				if (place(o.x, o.y) || temp[o.x][o.y])
					continue;
				else
				{
					temp[o.x][o.y] = 1;
					it.push(o);
				}
			}
		}
	}
	return -1;
}
int main()
{
	int xq, yq;
	while (~scanf("%d %d", &m, &n))
	{

		for (int i = 0; i<m; i++)
		{
			getchar();
			for (int j = 0; j<n; j++)
			{
				scanf("%c", &dt[i][j]);
				if (dt[i][j] == 'S')
				{
					xq = i; yq = j;
				}
			}
		}
		printf("%d\n", BFS(xq, yq));
	}
	return 0;
}