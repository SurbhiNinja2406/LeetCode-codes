# Definition for a binary tree node.
from collections import deque
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def trimBST(self, root, low, high):
        """
        :type root: Optional[TreeNode]
        :type low: int
        :type high: int
        :rtype: Optional[TreeNode]
        """
        if root is None:
            return None
        if root.val < low:
            return self.trimBST(root.right, low, high)
        if root.val > high:
            return self.trimBST(root.left, low, high)
        root.left = self.trimBST(root.left, low, high)
        root.right = self.trimBST(root.right, low, high)
        return root
def build_tree(values):
    if not values or values[0] is None:
        return None
    root = TreeNode(values[0])
    queue = deque([root])
    i = 1
    while queue and i < len(values):
        node = queue.popleft()
        if i < len(values):
            left_val = values[i]
            i += 1
            if left_val is not None:
                node.left = TreeNode(left_val)
                queue.append(node.left)
        if i < len(values):
            right_val = values[i]
            i += 1
            if right_val is not None:
                node.right = TreeNode(right_val)
                queue.append(node.right)
    return root
def tree_to_level_order(root):
    if root is None:
        return []
    result = []
    queue = deque([root])
    while queue:
        node = queue.popleft()
        if node is None:
            result.append(None)
        else:
            result.append(node.val)
            queue.append(node.left)
            queue.append(node.right)
    while result and result[-1] is None:
        result.pop()
    return result
if __name__ == "__main__":
    solution = Solution()
    root1 = build_tree([1, 0, 2])
    trimmed1 = solution.trimBST(root1, 1, 2)
    print("Example 1:")
    print("Input:  root = [1,0,2], low = 1, high = 2")
    print("Output:", tree_to_level_order(trimmed1))
    print("Expected: [1, None, 2]")
    print()
    root2 = build_tree([3, 0, 4, None, 2, None, None, 1])
    trimmed2 = solution.trimBST(root2, 1, 3)
    print("Example 2:")
    print("Input:  root = [3,0,4,null,2,null,null,1], low = 1, high = 3")
    print("Output:", tree_to_level_order(trimmed2))
    print("Expected: [3, 2, None, 1]")
    print()
    root3 = build_tree([5, 3, 8])
    trimmed3 = solution.trimBST(root3, 6, 10)
    print("Example 3 (extra):")
    print("Input:  root = [5,3,8], low = 6, high = 10")
    print("Output:", tree_to_level_order(trimmed3))
    print("Expected: [8]")
print(__name__)