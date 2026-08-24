# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: Optional[ListNode]
        :type k: int
        :rtype: Optional[ListNode]
        """
        node = head
        count = 0
        while node is not None and count < k:
            node = node.next
            count += 1
        if count < k:
            return head
        prev = self.reverseKGroup(node, k) 
        current = head
        for _ in range(k):
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        return prev
def build_linked_list(values):
    dummy = ListNode(0)
    current = dummy
    for v in values:
        current.next = ListNode(v)
        current = current.next
    return dummy.next
def linked_list_to_list(node):
    result = []
    while node:
        result.append(node.val)
        node = node.next
    return result
if __name__ == "__main__":
    sol = Solution()
    head = build_linked_list([1, 2, 3, 4, 5])
    result = sol.reverseKGroup(head, 2)
    print(linked_list_to_list(result))  
    head = build_linked_list([1, 2, 3, 4, 5])
    result = sol.reverseKGroup(head, 3)
    print(linked_list_to_list(result))  
    head = build_linked_list([1, 2, 3, 4])
    result = sol.reverseKGroup(head, 4)
    print(linked_list_to_list(result)) 
    head = build_linked_list([1, 2, 3])
    result = sol.reverseKGroup(head, 1)
    print(linked_list_to_list(result)) 
    head = build_linked_list([1])
    result = sol.reverseKGroup(head, 1)
    print(linked_list_to_list(result))  
    head = build_linked_list([1, 2, 3, 4, 5, 6])
    result = sol.reverseKGroup(head, 2)
    print(linked_list_to_list(result)) 
    head = build_linked_list([1, 2, 3, 4, 5, 6, 7])
    result = sol.reverseKGroup(head, 3)
    print(linked_list_to_list(result)) 
print(__name__)
        