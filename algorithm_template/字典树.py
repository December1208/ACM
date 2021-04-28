from typing import List, Optional


class Node:

    def __init__(self):
        self.is_end = False
        self.prefix_count = 0
        self.next_word: List[Optional[Node]] = [None for i in range(26)]


class Solution:

    def __init__(self):
        self.root = Node()

    def insert(self, word):
        root = self.root
        for char in word:
            index = ord(char) - ord('a')
            if root.next_word[index] is None:
                root.next_word[index] = Node()

            root = root.next_word[index]
            root.prefix_count += 1

        root.is_end = True

    def search(self, word):
        root = self.root
        for char in word:
            index = ord(char) - ord('a')
            if root.next_word[index]:
                root = root.next_word[index]
            else:
                return False

        if root.is_end:
            return True
        return False


if __name__ == '__main__':

    ts = Solution()
    ts.insert('abc')
    print(ts.search('abcd'))
