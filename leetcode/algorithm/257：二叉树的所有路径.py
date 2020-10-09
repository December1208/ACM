from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    """
    给定一个二叉树，返回所有从根节点到叶子节点的路径。
    """
    def binaryTreePaths(self, root: TreeNode) -> List[str]:

        def get_path(root: TreeNode, path: str):
            if root:
                path += str(root.val)
                if root.right or root.left:
                    path += '->'
                    get_path(root.left, path)
                    get_path(root.right, path)
                else:
                    result.append(path)

        result = []
        get_path(root, "")
        return result
