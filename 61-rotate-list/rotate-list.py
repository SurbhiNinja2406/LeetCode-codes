# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: Optional[ListNode]
        :type k: int
        :rtype: Optional[ListNode]
        """
        if not head or not head.next or k == 0:
            return head
        length = 1
        tail = head
        while tail.next:
            tail = tail.next
            length += 1
        k %= length        
        if k == 0:
            return head
        tail.next = head
        steps_to_new_tail = length - k - 1
        new_tail = head
        for _ in range(steps_to_new_tail):
            new_tail = new_tail.next        
        new_head = new_tail.next
        new_tail.next = None        
        return new_head
def build_linked_list(values):
    dummy = ListNode()
    current = dummy
    for v in values:
        current.next = ListNode(v)
        current = current.next
    return dummy.next
def linked_list_to_list(head):
    result = []
    while head:
        result.append(head.val)
        head = head.next
    return result
if __name__ == "__main__":
    solution = Solution()
    head1 = build_linked_list([1, 2, 3, 4, 5])
    k1 = 2
    result1 = solution.rotateRight(head1, k1)
    print(linked_list_to_list(result1))
    head2 = build_linked_list([0, 1, 2])
    k2 = 4
    result2 = solution.rotateRight(head2, k2)
    print(linked_list_to_list(result2))
        