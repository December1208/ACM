from typing import List, Optional


class Node:

    def __init__(self):
        self.is_end = False
        self.prefix_count = 0
        self.next_word: List[Optional[Node]] = [None for i in range(26)]

class Trie:


    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = Node()


    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        root = self.root
        for char in word:
            index = ord(char) - ord('a')
            if root.next_word[index] is None:
                root.next_word[index] = Node()

            root = root.next_word[index]
            root.prefix_count += 1

        root.is_end = True


    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
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



    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        root = self.root
        for char in prefix:
            index = ord(char) - ord('a')
            if root.next_word[index]:
                root = root.next_word[index]
            else:
                return False

        return True