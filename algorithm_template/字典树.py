from typing import List, Optional


class Node:

    def __init__(self):
        self.is_end = False
        self.prefix_count = 0
        self.next_word: List[Optional[Node]] = [None for i in range(26)]


class Solution:

    def __init__(self):
        self.root = Node()
        self.chara = [[0 for i in range(26)] for j in range(200001)]
        self.vis = [0 for i in range(200001)]
        self.e = 1

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

    def insert_list(self, word):
        p = 1
        for char in word:
            index = ord(char) - ord('a')
            if self.chara[p][index] == 0:
                self.e += 1
                self.chara[p][index] = self.e
                self.vis[self.e] = 0
            p = self.chara[p][index]
            self.vis[p] += 1

    def search_list(self, word):
        p = 1
        for char in word:
            index = ord(char) - ord('a')
            if self.chara[p][index] == 0:
                return False
            p = self.chara[p][index]

        return self.vis[p]


if __name__ == '__main__':

    ts = Solution()
    ts.insert('abc')
    print(ts.search('abcd'))
