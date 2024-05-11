# Problem: LRU Cache
# 一个哈希表配合一个双向链表实现LRU Cache



class LRUCache:

    class _DLinkNode:
        def __init__(self, key, value):
            self.key = key
            self.value = value
            self.next = None
            self.prev = None
        
        def __repr__(self):
            return f"key: {self.key}, value: {self.value}"

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.hash = {}
        self._dLinked_head = self._DLinkNode(-1, -1)
        self._dLinked_tail = self._DLinkNode(-1, -1)
        self._dLinked_head.next = self._dLinked_tail
        self._dLinked_tail.prev = self._dLinked_head
    
    def get(self, key: int) -> int:
        if key not in self.hash:
            return -1
        node = self.hash[key]
        node.prev.next = node.next
        node.next.prev = node.prev
        self._dLinked_head.next.prev = node
        node.next = self._dLinked_head.next
        self._dLinked_head.next = node
        node.prev = self._dLinked_head
        print(self._dLinked_tail.prev)
        return node.value

    def put(self, key: int, value: int) -> None:
        if key in self.hash:
           node = self.hash[key]
           node.value = value
           node.prev.next = node.next
           node.next.prev = node.prev
           self._dLinked_head.next.prev = node
           node.next = self._dLinked_head.next
           self._dLinked_head.next = node
           node.prev = self._dLinked_head
        else:
            if len(self.hash) == self.capacity:
                del self.hash[self._dLinked_tail.prev.key]
                # 这里记得不仅仅要删除哈希表中的元素，还要删除链表中的元素
                self._dLinked_tail.prev.prev.next = self._dLinked_tail
                self._dLinked_tail.prev = self._dLinked_tail.prev.prev
            node = self._DLinkNode(key, value)
            node.next = self._dLinked_head.next
            node.prev = self._dLinked_head
            self._dLinked_head.next.prev = node
            self._dLinked_head.next = node
            self.hash[key] = node
        print(self._dLinked_tail.prev)        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)

a = LRUCache(2)
a.put(1, 1)
a.put(2, 2)
print(a.get(1))
a.put(3, 3)
print(a.get(2))
a.put(4, 4)
print(a.get(1))
print(a.get(3))
print(a.get(4))
