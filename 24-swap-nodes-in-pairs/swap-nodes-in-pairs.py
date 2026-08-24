# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def swapPairs(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy
        while prev.next is not None and prev.next.next is not None:
            first = prev.next
            second = first.next
            first.next = second.next
            second.next = first
            prev.next = second
            prev = first
        return dummy.next
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
    head = build_linked_list([1, 2, 3, 4])
    result = sol.swapPairs(head)
    print(linked_list_to_list(result)) 
    head = build_linked_list([])
    result = sol.swapPairs(head)
    print(linked_list_to_list(result))  
    head = build_linked_list([1])
    result = sol.swapPairs(head)
    print(linked_list_to_list(result))  
    head = build_linked_list([1, 2, 3])
    result = sol.swapPairs(head)
    print(linked_list_to_list(result))  
    head = build_linked_list([1, 2])
    result = sol.swapPairs(head)
    print(linked_list_to_list(result))  
    head = build_linked_list([1, 2, 3, 4, 5, 6])
    result = sol.swapPairs(head)
    print(linked_list_to_list(result))
print(__name__)