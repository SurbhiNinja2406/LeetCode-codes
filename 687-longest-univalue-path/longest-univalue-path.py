# Definition for a binary tree node.
from collections import deque
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def longestUnivaluePath(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        self.max_len = 0
        def dfs(node):
            if node is None:
                return 0
            left_len = dfs(node.left)
            right_len = dfs(node.right)
            left_path = 0
            right_path = 0
            if node.left is not None and node.left.val == node.val:
                left_path = left_len + 1
            if node.right is not None and node.right.val == node.val:
                right_path = right_len + 1
            self.max_len = max(self.max_len, left_path + right_path)
            return max(left_path, right_path)
        dfs(root)
        return self.max_len
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
if __name__ == "__main__":
    solution = Solution()
    root1 = build_tree([5, 4, 5, 1, 1, None, 5])
    result1 = solution.longestUnivaluePath(root1)
    print("Example 1:")
    print("Input:  root = [5,4,5,1,1,null,5]")
    print("Output:", result1)
    print("Expected: 2")
    print()
    root2 = build_tree([1, 4, 5, 4, 4, None, 5])
    result2 = solution.longestUnivaluePath(root2)
    print("Example 2:")
    print("Input:  root = [1,4,5,4,4,null,5]")
    print("Output:", result2)
    print("Expected: 2")
    print()
    root3 = build_tree([])
    result3 = solution.longestUnivaluePath(root3)
    print("Example 3 (extra):")
    print("Input:  root = []")
    print("Output:", result3)
    print("Expected: 0")
    print()
    root4 = build_tree([7])
    result4 = solution.longestUnivaluePath(root4)
    print("Example 4 (extra):")
    print("Input:  root = [7]")
    print("Output:", result4)
    print("Expected: 0")
    print()
    root5 = build_tree([2, 2, 2, 2, 2, 2, 2])
    result5 = solution.longestUnivaluePath(root5)
    print("Example 5 (extra):")
    print("Input:  root = [2,2,2,2,2,2,2]")
    print("Output:", result5)
    print("Expected: 4")
print(__name__)