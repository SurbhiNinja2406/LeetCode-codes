from sortedcontainers import SortedList
class Node:
    __slots__ = ("val", "seq", "prev", "next")
    def __init__(self, val, seq):
        self.val = val
        self.seq = seq
        self.prev = None
        self.next = None
class MaxStack(object):
    def __init__(self):
        self.head = Node(None, None)
        self.tail = Node(None, None)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.sorted_vals = SortedList()
        self.seq_to_node = {}
        self.seq_counter = 0
    def _insert_node(self, node):
        prev = self.tail.prev
        prev.next = node
        node.prev = prev
        node.next = self.tail
        self.tail.prev = node
    def _remove_node(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev
    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        node = Node(x, self.seq_counter)
        self._insert_node(node)
        self.sorted_vals.add((x, self.seq_counter))
        self.seq_to_node[self.seq_counter] = node
        self.seq_counter += 1
    def pop(self):
        """
        :rtype: int
        """
        node = self.tail.prev 
        self._remove_node(node)
        self.sorted_vals.remove((node.val, node.seq))
        del self.seq_to_node[node.seq]
        return node.val
    def top(self):
        """
        :rtype: int
        """
        return self.tail.prev.val
    def peekMax(self):
        """
        :rtype: int
        """
        return self.sorted_vals[-1][0]
    def popMax(self):
        """
        :rtype: int
        """
        val, seq = self.sorted_vals.pop() 
        node = self.seq_to_node.pop(seq)
        self._remove_node(node) 
        return val
if __name__ == "__main__":
    stk = MaxStack()
    stk.push(5)
    stk.push(1)
    stk.push(5)
    results = []
    results.append(stk.top())     
    results.append(stk.popMax())   
    results.append(stk.top())     
    results.append(stk.peekMax()) 
    results.append(stk.pop())   
    results.append(stk.top())   
    print("Results: ", results)
    print("Expected: [5, 5, 1, 5, 1, 5]")
    assert results == [5, 5, 1, 5, 1, 5], "Mismatch!"
    print("Test passed!\n")
    stk2 = MaxStack()
    stk2.push(3)
    stk2.push(7)
    stk2.push(7)
    stk2.push(2)
    print("Extra test - popMax:", stk2.popMax()) 
    print("Extra test - top after:", stk2.top())  
    print("Extra test - popMax again:", stk2.popMax()) 
    print("Extra test - top after:", stk2.top())
    stk3 = MaxStack()
    stk3.push(42)
    print("Single element top:", stk3.top())       
    print("Single element peekMax:", stk3.peekMax()) 
    print("Single element popMax:", stk3.popMax())   
print(__name__)