from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = {}
        for item in strs:
            str_key = self.convert_str(item)
            value = result.get(str_key, [])
            value.append(item)
            result[str_key] = value
        return list(result.values())

    def convert_str(self, str_: str) -> str:
        result = [0] * 26
        for char in str_:
            result[ord(char)-ord('a')] += 1
        return ','.join([f"{index}{count}" for index, count in enumerate(result) if count != 0])


if __name__ == '__main__':

    s = Solution()
    res = s.groupAnagrams(['bac', 'abc', 'kkk'])
    print(res)
