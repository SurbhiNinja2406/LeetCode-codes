# Definition for singly-linked list.
# Definition for singly-linked list.
#class ListNode(object):
#    def __init__(self, val=0, next=None):
#        self.val = val
#        self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        dummy = ListNode(0)
        current = dummy
        carry = 0
        while l1 is not None or l2 is not None or carry:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            total = val1 + val2 + carry
            carry = total // 10
            digit = total % 10
            current.next = ListNode(digit)
            current = current.next
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
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
    l1 = build_linked_list([2, 4, 3])
    l2 = build_linked_list([5, 6, 4])
    result = sol.addTwoNumbers(l1, l2)
    print(linked_list_to_list(result)) 
    l1 = build_linked_list([0])
    l2 = build_linked_list([0])
    result = sol.addTwoNumbers(l1, l2)
    print(linked_list_to_list(result))
    l1 = build_linked_list([9, 9, 9, 9, 9, 9])
    l2 = build_linked_list([9, 9, 9, 9])
    result = sol.addTwoNumbers(l1, l2)
    print(linked_list_to_list(result)) 
print(__name__)