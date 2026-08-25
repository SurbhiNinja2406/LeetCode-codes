# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        current = head
        while current and current.next:
            if current.val == current.next.val:
                current.next = current.next.next 
            else:
                current = current.next
        return head
def build_list(values):
    dummy = ListNode(0)
    tail = dummy
    for v in values:
        tail.next = ListNode(v)
        tail = tail.next
    return dummy.next
def list_to_array(node):
    result = []
    while node:
        result.append(node.val)
        node = node.next
    return result
if __name__ == "__main__":
    sol = Solution()
    head1 = build_list([1, 1, 2])
    result1 = sol.deleteDuplicates(head1)
    print(list_to_array(result1))  
    head2 = build_list([1, 1, 2, 3, 3])
    result2 = sol.deleteDuplicates(head2)
    print(list_to_array(result2)) 
    head3 = build_list([])
    result3 = sol.deleteDuplicates(head3)
    print(list_to_array(result3)) 
print(__name__)