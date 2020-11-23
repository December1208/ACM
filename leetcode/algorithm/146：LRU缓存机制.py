class Node(object):

    __slots__ = ["key", "value", "prev", "next"]

    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None


class LRUCache(object):

    def __init__(self, capacity=0):

        self.dic = {}
        self.capacity = capacity
        self.head = Node(-1, -1)
        self.tail = Node(-1, -1)

        self.head.next = self.tail
        self.tail.prev = self.head
        self.size = 0

    def get(self, key, default=None):
        if key not in self.dic:
            return default

        node = self.dic[key]
        self.move_to_head(node)
        return node.value

    def put(self, key, value):
        if key not in self.dic:
            node = Node(key=key, value=value)
            self.dic[key] = node
            self.add_to_head(node)
            self.size += 1
            if self.size > self.capacity:
                removed = self.remove_tail()
                self.dic.pop(removed.key)
                self.size -= 1
        else:
            node = self.dic[key]
            node.value = value
            self.move_to_head(node)

    def remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

    def remove_tail(self):
        node = self.tail.prev
        self.remove(node)
        return node

    def move_to_head(self, node):
        self.remove(node)
        self.add_to_head(node)

    def add_to_head(self, node):
        node.prev = self.head
        node.next = self.head.next
        self.head.next.prev = node
        self.head.next = node


if __name__ == "__main__":
    dic = LRUCache(3)
    dic.put('a', 1)
    dic.put('b', 2)
    dic.put('c', 3)
    dic.put('d', 4)

    print(dic.get('a'))
