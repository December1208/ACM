from typing import List
import collections
import heapq


class Solution:
    """
    给定一个机票的字符串二维数组 [from, to]，子数组中的两个成员分别表示飞机出发和降落的机场地点，
    对该行程进行重新规划排序。所有这些机票都属于一个从 JFK（肯尼迪国际机场）出发的先生，所以该行程必须从 JFK 开始
    """
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        def dfs(curr: str):
            while vec[curr]:
                tmp = heapq.heappop(vec[curr])
                dfs(tmp)
            stack.append(curr)

        vec = collections.defaultdict(list)
        for depart, arrive in tickets:
            vec[depart].append(arrive)
        for key in vec:
            heapq.heapify(vec[key])

        stack = list()
        dfs("JFK")
        return stack[::-1]


print(Solution().findItinerary([["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"], ["MUC", "LHR"]]))
