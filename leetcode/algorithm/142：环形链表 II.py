class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    """
    给定一个链表，返回链表开始入环的第一个节点。 如果链表无环，则返回 null。
    为了表示给定链表中的环，我们使用整数 pos 来表示链表尾连接到链表中的位置（索引从 0 开始）。 如果 pos 是 -1，则在该链表中没有环。
    """
    def detectCycle(self, head: ListNode) -> ListNode:
        slow, fast = head, head
        while fast is not None:
            slow = slow.next
            if fast.next is None:
                return None
            fast = fast.next.next
            if slow == fast:
                n_head = head
                while n_head != slow:
                    n_head = n_head.next
                    slow = slow.next
                return slow

        return None

