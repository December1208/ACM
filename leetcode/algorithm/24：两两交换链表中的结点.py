class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    """
    给定一个链表，两两交换其中相邻的节点，并返回交换后的链表。
    你不能只是单纯的改变节点内部的值，而是需要实际的进行节点交换。
    """
    def swapPairs(self, head: ListNode) -> ListNode:
        newNode = ListNode()
        left, right, temp = head, head, newNode
        if head is None or head.next is None:
            return head
        temp.next = left
        while left is not None and left.next is not None:
            right = left.next
            temp.next = right
            left.next = right.next
            right.next = left
            temp = left
            left = left.next
        return newNode.next
