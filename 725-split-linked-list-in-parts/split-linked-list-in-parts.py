# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def splitListToParts(self, head, k):
        """
        :type head: Optional[ListNode]
        :type k: int
        :rtype: List[Optional[ListNode]]
        """
        length = 0
        node = head
        while node:
            length += 1
            node = node.next
        base_size, extra = divmod(length, k)        
        result = []
        current = head
        for i in range(k):
            part_size = base_size + (1 if i < extra else 0)            
            if part_size == 0:
                result.append(None)
                continue            
            part_head = current            
            for _ in range(part_size - 1):
                current = current.next            
            next_part_start = current.next
            current.next = None            
            current = next_part_start            
            result.append(part_head)        
        return result
def build_linked_list(values):
    dummy = ListNode()
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
def parts_to_list_of_lists(parts):
    return [linked_list_to_list(part) for part in parts]
if __name__ == "__main__":
    solution = Solution()
    head1 = build_linked_list([1, 2, 3])
    k1 = 5
    result1 = solution.splitListToParts(head1, k1)
    print("Example 1:")
    print("Input: head = [1,2,3], k = 5")
    print("Output:", parts_to_list_of_lists(result1))
    print("Expected: [[1], [2], [3], [], []]")
    print()
    head2 = build_linked_list([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    k2 = 3
    result2 = solution.splitListToParts(head2, k2)
    print("Example 2:")
    print("Input: head = [1,2,3,4,5,6,7,8,9,10], k = 3")
    print("Output:", parts_to_list_of_lists(result2))
    print("Expected: [[1,2,3,4], [5,6,7], [8,9,10]]")
    print()
    head3 = build_linked_list([])
    k3 = 3
    result3 = solution.splitListToParts(head3, k3)
    print("Extra Test (empty list):")
    print("Input: head = [], k = 3")
    print("Output:", parts_to_list_of_lists(result3))
    print("Expected: [[], [], []]")
    print()
    head4 = build_linked_list([1, 2, 3, 4, 5])
    k4 = 1
    result4 = solution.splitListToParts(head4, k4)
    print("Extra Test (k = 1):")
    print("Input: head = [1,2,3,4,5], k = 1")
    print("Output:", parts_to_list_of_lists(result4))
    print("Expected: [[1,2,3,4,5]]")
print(__name__)