# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def nextLargerNodes(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: List[int]
        """
        values = []
        node = head
        while node:
            values.append(node.val)
            node = node.next
        n = len(values)
        answer = [0] * n
        stack = []
        for i, val in enumerate(values):
            while stack and values[stack[-1]] < val:
                idx = stack.pop()
                answer[idx] = val
            stack.append(i)
        return answer
def build_linked_list(values):
    dummy = ListNode()
    current = dummy
    for v in values:
        current.next = ListNode(v)
        current = current.next
    return dummy.next
if __name__ == "__main__":
    sol = Solution()
    test_cases = [
        ([2, 1, 5], [5, 5, 0]),
        ([2, 7, 4, 3, 5], [7, 0, 5, 5, 0]),
        ([1, 7, 5, 1, 9, 2, 5, 1], [7, 9, 9, 9, 0, 5, 0, 0]),
        ([1], [0]),
        ([5, 4, 3, 2, 1], [0, 0, 0, 0, 0]),
    ]
    for values, expected in test_cases:
        head = build_linked_list(values)
        result = sol.nextLargerNodes(head)
        status = "PASS" if result == expected else "FAIL"
        print("values={0} -> {1} (expected {2}) [{3}]".format(
            values, result, expected, status
        ))
print(__name__)