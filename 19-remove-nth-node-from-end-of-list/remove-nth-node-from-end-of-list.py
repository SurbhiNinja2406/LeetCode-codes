# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: Optional[ListNode]
        :type n: int
        :rtype: Optional[ListNode]
        """
        dummy = ListNode(0)
        dummy.next = head
        fast = dummy
        slow = dummy
        for _ in range(n + 1):
            fast = fast.next
        while fast is not None:
            fast = fast.next
            slow = slow.next
        slow.next = slow.next.next
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
    head = build_linked_list([1, 2, 3, 4, 5])
    result = sol.removeNthFromEnd(head, 2)
    print(linked_list_to_list(result))  
    head = build_linked_list([1])
    result = sol.removeNthFromEnd(head, 1)
    print(linked_list_to_list(result)) 
    head = build_linked_list([1, 2])
    result = sol.removeNthFromEnd(head, 1)
    print(linked_list_to_list(result))  
    head = build_linked_list([1, 2, 3])
    result = sol.removeNthFromEnd(head, 3)
    print(linked_list_to_list(result)) 
    head = build_linked_list([1, 2, 3])
    result = sol.removeNthFromEnd(head, 1)
    print(linked_list_to_list(result)) 
    head = build_linked_list([1, 2])
    result = sol.removeNthFromEnd(head, 2)
    print(linked_list_to_list(result)) 