# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sortedListToBST(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[TreeNode]
        """
        values = []
        node = head
        while node:
            values.append(node.val)
            node = node.next
        def build(left, right):
            if left > right:
                return None
            mid = (left + right) // 2
            root = TreeNode(values[mid])
            root.left = build(left, mid - 1)
            root.right = build(mid + 1, right)
            return root
        return build(0, len(values) - 1)
def build_linked_list(values):
    dummy = ListNode()
    current = dummy
    for v in values:
        current.next = ListNode(v)
        current = current.next
    return dummy.next
def tree_to_list(root):
    if not root:
        return []
    result = []
    queue = [root]
    while queue:
        node = queue.pop(0)
        if node:
            result.append(node.val)
            queue.append(node.left)
            queue.append(node.right)
        else:
            result.append(None)
    while result and result[-1] is None:
        result.pop()
    return result
if __name__ == "__main__":
    sol = Solution()
    head1 = build_linked_list([-10, -3, 0, 5, 9])
    root1 = sol.sortedListToBST(head1)
    print("Test 1: {}".format(tree_to_list(root1)))
    head2 = build_linked_list([])
    root2 = sol.sortedListToBST(head2)
    print("Test 2: {}".format(tree_to_list(root2))) 