# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def insertionSortList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if not head or not head.next:
            return head
        dummy = ListNode(0)
        dummy.next = head
        sorted_last = head
        current = head.next        
        while current:
            if sorted_last.val <= current.val:
                sorted_last = sorted_last.next
            else:
                sorted_last.next = current.next
                prev = dummy
                while prev.next.val <= current.val:
                    prev = prev.next
                current.next = prev.next
                prev.next = current
            current = sorted_last.next        
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
    result1 = sol.insertionSortList(head1)
    print(linked_list_to_list(result1))  
    head2 = build_linked_list([-1, 5, 3, 4, 0])
    result2 = sol.insertionSortList(head2)
    print(linked_list_to_list(result2))
print(__name__)