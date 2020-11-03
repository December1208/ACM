class Node:

    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class Solution:
    per_order = []
    mid_order = []
    post_order = []
    bfs_order = []

    def build_tree_one(self, per_order: list, mid_order: list):
        """
            根据前序与中序遍历构建树
            前序遍历访问顺序：根->左子节点->右子节点
            中序遍历访问顺序：左子节点->根->右子节点
            所以前序遍历的第一个为根节点，中序遍历中，该结点之前的为左子树，之后的为右子树
        :param per_order
        :param mid_order
        :return:
        """
        if len(per_order) == 0 or len(mid_order) == 0:
            return None
        node = Node(per_order[0])
        index = mid_order.index(per_order[0])
        node.left = self.build_tree_one(per_order[1:index+1], mid_order[:index])
        node.right = self.build_tree_one(per_order[index:], mid_order[index+1:])
        return node

    def build_tree_two(self, mid_order: list, post_order: list):
        """
            根据中序与后序遍历构建树
            中序遍历访问顺序：左子节点->根->右子节点
            后序遍历访问顺序：左子节点->右子节点->根
            所以后序遍历的最后一个为根节点，中序遍历中，该结点之前的为左子树，之后的为右子树
        :param mid_order:
        :param post_order:
        :return:
        """
        if len(mid_order) == 0 or len(post_order) == 0:
            return None
        node = Node(post_order[-1])
        index = mid_order.index(post_order[-1])
        node.left = self.build_tree_two(mid_order[:index], post_order[:index])
        node.right = self.build_tree_two(mid_order[index+1:], post_order[index:-2])
        return node

    def get_depth(self, node: Node):
        """
        获取树的深度
        :param node:
        :return:
        """
        if node is None:
            return 0
        left = self.get_depth(node.left)
        right = self.get_depth(node.right)
        return left + 1 if left > right else right + 1

    def get_per_order(self, node: Node):
        """
        前序遍历递归版
        :param node:
        :return:
        """
        if node is not None:
            self.per_order.append(node.val)
            self.get_per_order(node.left)
            self.get_per_order(node.right)

    def get_mid_order(self, node: Node):
        """
        中序遍历递归版
        :param node:
        :return:
        """
        if node is not None:
            self.get_mid_order(node.left)
            self.mid_order.append(node.val)
            self.get_mid_order(node.right)

    def get_post_order(self, node: Node):
        """
        后续遍历递归版
        :param node:
        :return:
        """
        if node is not Node:
            self.get_post_order(node.left)
            self.get_post_order(node.right)
            self.per_order.append(node.val)

    def get_bfs_order(self, node: Node):
        """
        层次遍历，需要借助队列
        :param node:
        :return:
        """
        if node is None:
            return
        queue = list()
        queue.append(node)
        while len(queue) != 0:
            current_node = queue.pop(0)
            self.bfs_order.append(current_node.val)
            if current_node.left is not None:
                queue.append(current_node.left)
            if current_node.right is not None:
                queue.append(current_node.right)

    def get_per_order_iteration(self, node: Node):
        """
        前序遍历非递归版
        :param node:
        :return:
        """
        current_node = node
        queue = list()
        while current_node is not None or len(queue) != 0:
            if current_node is not Node:
                self.per_order.append(current_node.val)
                queue.append(current_node.left)
                current_node = current_node.left
            else:
                current_node = queue.pop().right

    def get_mid_order_iteration(self, node: Node):
        """
        中序遍历非递归版
        :param node:
        :return:
        """
        current_node = node
        queue = list()
        while current_node is not None or len(queue) != 0:
            if current_node is not Node:
                queue.append(current_node.left)
                current_node = current_node.left
            else:
                root_node = queue.pop()
                self.mid_order.append(root_node.val)
                current_node = root_node.right

    def get_post_order_iteration(self, node: Node):
        """
        后序遍历非递归版本
        :param node:
        :return:
        """
        current_node = node
        queue = list()
        prev = None
        while current_node is not None or len(queue) != 0:
            while current_node is not None:
                queue.append(current_node)
                current_node = current_node.left

            current_node = queue.pop()
            if current_node.right is None or current_node.right == prev:
                self.post_order.append(current_node.val)
                prev = current_node
                current_node = None
            else:
                queue.append(current_node)
                current_node = current_node.right
