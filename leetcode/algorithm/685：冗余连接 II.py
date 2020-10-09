from typing import List


class UnionSet:
    """
    这里采用了路径压缩，即从指向上一级直接指向了根结点。
    """
    def __init__(self, n: int):
        self.union_set = list(range(n))

    def find(self, node):
        if self.union_set[node] != node:
            self.union_set[node] = self.find(self.union_set[node])

        return self.union_set[node]

    def union(self, node1: int, node2: int):
        self.union_set[self.find(node1)] = self.find(node2)


class Solution:
    """
    在本问题中，有根树指满足以下条件的有向图。该树只有一个根节点，所有其他节点都是该根节点的后继。每一个节点只有一个父节点，除了根节点没有父节点。
    输入一个有向图，该图由一个有着N个节点 (节点值不重复1, 2, ..., N) 的树及一条附加的边构成。附加的边的两个顶点包含在1到N中间，
    这条附加的边不属于树中已存在的边。结果图是一个以边组成的二维数组。 每一个边 的元素是一对 [u, v]，用以表示有向图中连接顶点 u 和顶点 v 的边，
    其中 u 是 v 的一个父节点。返回一条能删除的边，使得剩下的图是有N个节点的有根树。若有多个答案，返回最后出现在给定二维数组的答案。

    采用并查集解决，如果要构成图，则N个点需要有N-1个边，本题提供了N个边，需要删除掉一条边
    那么会有两种情况：
        - 若每个结点都只有一个父节点，那么，肯定出现了一个环路
        - 附加的边指向非根结点，那么就会出现一个结点有两个根节点，此时可能会有环路，也可能没有环路
    - 第一种情况，直接删除冲突边即可
    - 第二种情况，要看是出现了环路还是没有环路分别处理
    """
    def findRedundantDirectedConnection(self, edges: List[List[int]]) -> List[int]:

        nodeCount = len(edges)
        unionSet = UnionSet(nodeCount+1)
        parent = list(range(nodeCount+1))
        conflict = -1
        cycle = -1
        for i, (node1, node2) in enumerate(edges):
            if parent[node2] != node2:
                conflict = i
            else:
                parent[node2] = node1
                if unionSet.find(node2) != unionSet.find(node1):
                    unionSet.union(node1, node2)
                else:
                    cycle = i
        if conflict < 0:
            return [edges[cycle][0], edges[cycle][1]]
        else:
            conflictEdge = edges[conflict]
            if cycle >= 0:
                return [parent[conflictEdge[1]], conflictEdge[1]]
            else:
                return [conflictEdge[0], conflictEdge[1]]
