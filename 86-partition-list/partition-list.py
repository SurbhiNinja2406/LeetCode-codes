# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def partition(self, head, x):
        """
        :type head: Optional[ListNode]
        :type x: int
        :rtype: Optional[ListNode]
        """
        less_dummy = ListNode(0)
        greater_dummy = ListNode(0)
        less_tail = less_dummy
        greater_tail = greater_dummy
        current = head
        while current:
            if current.val < x:
                less_tail.next = current
                less_tail = less_tail.next
            else:
                greater_tail.next = current
                greater_tail = greater_tail.next
            current = current.next
        greater_tail.next = None 
        less_tail.next = greater_dummy.next
        return less_dummy.next
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
    head1 = build_list([1, 4, 3, 2, 5, 2])
    result1 = sol.partition(head1, 3)
    print(list_to_array(result1)) 
    head2 = build_list([2, 1])
    result2 = sol.partition(head2, 2)
    print(list_to_array(result2))
print(__name__)