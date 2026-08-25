# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reorderList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: None Do not return anything, modify head in-place instead.
        """
        if not head or not head.next:
            return
        slow, fast = head, head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        second = slow.next
        slow.next = None 
        prev = None
        while second:
            next_node = second.next
            second.next = prev
            prev = second
            second = next_node
        second = prev  
        first = head
        while second:
            first_next = first.next
            second_next = second.next            
            first.next = second
            second.next = first_next            
            first = first_next
            second = second_next
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
    head1 = build_linked_list([1, 2, 3, 4])
    sol.reorderList(head1)
    print(linked_list_to_list(head1))  
    head2 = build_linked_list([1, 2, 3, 4, 5])
    sol.reorderList(head2)
    print(linked_list_to_list(head2)) 
print(__name__)