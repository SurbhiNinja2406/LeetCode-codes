# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def numComponents(self, head, nums):
        """
        :type head: Optional[ListNode]
        :type nums: List[int]
        :rtype: int
        """
        num_set = set(nums)
        count = 0
        in_component = False  
        node = head
        while node:
            if node.val in num_set:
                if not in_component:
                    count += 1
                    in_component = True
            else:
                in_component = False
            node = node.next
        return count
def build_linked_list(values):
    dummy = ListNode(0)
    current = dummy
    for v in values:
        current.next = ListNode(v)
        current = current.next
    return dummy.next
if __name__ == "__main__":
    solution = Solution()
    test_cases = [
        ([0, 1, 2, 3], [0, 1, 3], 2),
        ([0, 1, 2, 3, 4], [0, 3, 1, 4], 2),
    ]
    for head_values, nums, expected in test_cases:
        head = build_linked_list(head_values)
        result = solution.numComponents(head, list(nums))
        status = "PASS" if result == expected else "FAIL"
        print("head={:<20} nums={:<15} expected={} got={} [{}]".format(
            str(head_values), str(nums), expected, result, status))
print(__name__)