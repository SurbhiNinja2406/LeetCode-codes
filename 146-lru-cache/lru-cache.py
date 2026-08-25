class Node(object):
    """A node in the doubly linked list, storing a key-value pair."""
    def __init__(self, key=0, value=0):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None


class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.cache = {}  # maps key -> Node
        
        # Dummy head and tail nodes to avoid edge-case checks when
        # adding/removing nodes at the boundaries of the list.
        # Order convention: head.next = most recently used, tail.prev = least recently used
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head

    def _remove(self, node):
        """Detach a node from the linked list."""
        prev_node = node.prev
        next_node = node.next
        prev_node.next = next_node
        next_node.prev = prev_node

    def _add_to_front(self, node):
        """Insert a node right after head (marking it as most recently used)."""
        node.prev = self.head
        node.next = self.head.next
        self.head.next.prev = node
        self.head.next = node

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key not in self.cache:
            return -1        
        node = self.cache[key]
        self._remove(node)
        self._add_to_front(node)        
        return node.value
    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        if key in self.cache:
            node = self.cache[key]
            node.value = value
            self._remove(node)
            self._add_to_front(node)
        else:
            if len(self.cache) >= self.capacity:
                lru_node = self.tail.prev
                self._remove(lru_node)
                del self.cache[lru_node.key]            
            new_node = Node(key, value)
            self.cache[key] = new_node
            self._add_to_front(new_node)
if __name__ == "__main__":
    lRUCache = LRUCache(2)
    lRUCache.put(1, 1)         
    lRUCache.put(2, 2)         
    print(lRUCache.get(1))     
    lRUCache.put(3, 3)          
    print(lRUCache.get(2))     
    lRUCache.put(4, 4)         
    print(lRUCache.get(1))     
    print(lRUCache.get(3))    
    print(lRUCache.get(4))    
print(__name__)
# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)