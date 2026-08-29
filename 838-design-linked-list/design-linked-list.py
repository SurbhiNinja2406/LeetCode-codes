class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
class MyLinkedList(object):
    def __init__(self):
        self.head = None
        self.size = 0
    def get(self, index):
        """
        :type index: int
        :rtype: int
        """
        if index < 0 or index >= self.size:
            return -1
        curr = self.head
        for _ in range(index):
            curr = curr.next
        return curr.val
    def addAtHead(self, val):
        """
        :type val: int
        :rtype: None
        """
        self.addAtIndex(0, val)
    def addAtTail(self, val):
        """
        :type val: int
        :rtype: None
        """
        self.addAtIndex(self.size, val)
    def addAtIndex(self, index, val):
        """
        :type index: int
        :type val: int
        :rtype: None
        """
        if index > self.size:
            return
        if index < 0:
            index = 0
        new_node = Node(val)
        if index == 0:
            new_node.next = self.head
            self.head = new_node
        else:
            prev = self.head
            for _ in range(index - 1):
                prev = prev.next
            new_node.next = prev.next
            prev.next = new_node
        self.size += 1
    def deleteAtIndex(self, index):
        """
        :type index: int
        :rtype: None
        """
        if index < 0 or index >= self.size:
            return
        if index == 0:
            self.head = self.head.next
        else:
            prev = self.head
            for _ in range(index - 1):
                prev = prev.next
            prev.next = prev.next.next
        self.size -= 1
if __name__ == "__main__":
    operations = ["MyLinkedList", "addAtHead", "addAtTail", "addAtIndex",
                  "get", "deleteAtIndex", "get"]
    arguments = [[], [1], [3], [1, 2], [1], [1], [1]]
    obj = None
    results = []
    for op, args in zip(operations, arguments):
        if op == "MyLinkedList":
            obj = MyLinkedList()
            results.append(None)
        elif op == "get":
            results.append(obj.get(*args))
        elif op == "addAtHead":
            obj.addAtHead(*args)
            results.append(None)
        elif op == "addAtTail":
            obj.addAtTail(*args)
            results.append(None)
        elif op == "addAtIndex":
            obj.addAtIndex(*args)
            results.append(None)
        elif op == "deleteAtIndex":
            obj.deleteAtIndex(*args)
            results.append(None)
    print("Output:  ", results)
    print("Expected:", [None, None, None, None, 2, None, 3])
    assert results == [None, None, None, None, 2, None, 3], "Mismatch!"
    print("Test passed!")
    ll = MyLinkedList()
    print("\nExtra tests:")
    print(ll.get(0))       
    ll.addAtIndex(5, 10)    
    print(ll.get(0))      
    ll.addAtTail(10)
    ll.addAtTail(20)
    ll.addAtTail(30)      
    ll.deleteAtIndex(1)  
    print(ll.get(0), ll.get(1)) 
    ll.addAtIndex(1, 25)     
    print(ll.get(1))       
    ll.deleteAtIndex(0)    
    print(ll.get(0))      
print(__name__)