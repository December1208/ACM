from math import inf


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def minDiffInBST(self, root: TreeNode) -> int:
        self.result, self.value = inf, -1
        self.dfs(root)
        return self.result

    def dfs(self, root: TreeNode):
        if root is None:
            return
        self.dfs(root.left)
        if self.value == -1:
            self.value = root.val
        else:
            self.result = min(self.result, root.val - self.value)
            self.value = root.val
        self.dfs(root.right)
