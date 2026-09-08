# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def middleNode(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow
def build_linked_list(values):
    dummy = ListNode()
    current = dummy
    for val in values:
        current.next = ListNode(val)
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
    middle1 = solution.middleNode(head1)
    print("Example 1 Input:  [1,2,3,4,5]")
    print("Example 1 Output:", linked_list_to_list(middle1))  
    print()
    head2 = build_linked_list([1, 2, 3, 4, 5, 6])
    middle2 = solution.middleNode(head2)
    print("Example 2 Input:  [1,2,3,4,5,6]")
    print("Example 2 Output:", linked_list_to_list(middle2))  
    print()
    head3 = build_linked_list([1])
    middle3 = solution.middleNode(head3)
    print("Example 3 Input:  [1]")
    print("Example 3 Output:", linked_list_to_list(middle3))
    print()
    head4 = build_linked_list([1, 2])
    middle4 = solution.middleNode(head4)
    print("Example 4 Input:  [1,2]")
    print("Example 4 Output:", linked_list_to_list(middle4))  
print(__name__)