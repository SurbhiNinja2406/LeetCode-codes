# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def sortList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if not head or not head.next:
            return head
        prev = None
        slow = head
        fast = head        
        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next        
        prev.next = None 
        left = self.sortList(head)
        right = self.sortList(slow)
        return self._merge(left, right)    
    def _merge(self, l1, l2):
        dummy = ListNode(0)
        tail = dummy        
        while l1 and l2:
            if l1.val <= l2.val:
                tail.next = l1
                l1 = l1.next
            else:
                tail.next = l2
                l2 = l2.next
            tail = tail.next
        tail.next = l1 if l1 else l2
        return dummy.next
def build_linked_list(values):
    if not values:
        return None    
    head = ListNode(values[0])
    current = head
    for v in values[1:]:
        current.next = ListNode(v)
        current = current.next    
    return head
def linked_list_to_list(head):
    result = []
    current = head
    while current:
        result.append(current.val)
        current = current.next
    return result
if __name__ == "__main__":
    sol = Solution()
    head1 = build_linked_list([4, 2, 1, 3])
    result1 = sol.sortList(head1)
    print(linked_list_to_list(result1))  
    head2 = build_linked_list([-1, 5, 3, 4, 0])
    result2 = sol.sortList(head2)
    print(linked_list_to_list(result2))  
    head3 = build_linked_list([])
    result3 = sol.sortList(head3)
    print(linked_list_to_list(result3)) 
print(__name__)