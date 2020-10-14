from collections import Counter
from typing import List


class Solution:
    """
    给定仅有小写字母组成的字符串数组 A，返回列表中的每个字符串中都显示的全部字符（包括重复字符）组成的列表。
    例如，如果一个字符在每个字符串中出现 3 次，但不是 4 次，则需要在最终答案中包含该字符 3 次。
    你可以按任意顺序返回答案。
    """
    def commonChars(self, A: List[str]) -> List[str]:
        res = None
        for s in A:
            temp = Counter(s)
            if res is None:
                res = temp
            else:
                res &= temp
        return list(res.elements())


print(Solution().commonChars(["bella", "label", "roller"]))
