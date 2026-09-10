# Definition for a binary tree node.
from collections import deque
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def increasingBST(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: Optional[TreeNode]
        """
        dummy = TreeNode(-1)
        self.prev = dummy
        def inorder(node):
            if node is None:
                return
            inorder(node.left)
            node.left = None
            self.prev.right = node
            self.prev = node
            inorder(node.right)
        inorder(root)
        return dummy.right
def build_tree(values):
    if not values or values[0] is None:
        return None
    it = iter(values)
    root_val = next(it)
    root = TreeNode(root_val)
    queue = deque([root])
    while queue:
        node = queue.popleft()
        try:
            val = next(it)
        except StopIteration:
            break
        if val is not None:
            node.left = TreeNode(val)
            queue.append(node.left)
        try:
            val = next(it)
        except StopIteration:
            break
        if val is not None:
            node.right = TreeNode(val)
            queue.append(node.right)
    return root
def tree_to_list(root):
    if root is None:
        return []
    result = []
    queue = deque([root])
    while queue:
        node = queue.popleft()
        if node is None:
            result.append(None)
            continue
        result.append(node.val)
        queue.append(node.left)
        queue.append(node.right)
    while result and result[-1] is None:
        result.pop()
    return result
if __name__ == "__main__":
    solution = Solution()
    input1 = [5, 3, 6, 2, 4, None, 8, 1, None, None, None, 7, 9]
    root1 = build_tree(input1)
    result1 = solution.increasingBST(root1)
    print("Example 1:")
    print("Input: ", input1)
    print("Output:", tree_to_list(result1))
    print()
    input2 = [5, 1, 7]
    root2 = build_tree(input2)
    result2 = solution.increasingBST(root2)
    print("Example 2:")
    print("Input: ", input2)
    print("Output:", tree_to_list(result2))
print(__name__)