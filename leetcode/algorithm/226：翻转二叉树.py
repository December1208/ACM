class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        def reverse_tree(node: TreeNode):
            if node is None:
                return
            reverse_tree(node.left)
            reverse_tree(node.right)
            node.right, node.left = node.left, node.right

        reverse_tree(root)
        return root
