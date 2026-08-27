# Definition for a binary tree node.
from collections import deque
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def findSecondMinimumValue(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        self.result = -1
        smallest = root.val
        def dfs(node):
            if node is None:
                return
            if node.val > smallest:
                if self.result == -1 or node.val < self.result:
                    self.result = node.val
                return
            dfs(node.left)
            dfs(node.right)
        dfs(root)
        return self.result
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
    root1 = build_tree([2, 2, 5, None, None, 5, 7])
    result1 = solution.findSecondMinimumValue(root1)
    print("Example 1:")
    print("Input:  root = [2,2,5,null,null,5,7]")
    print("Output:", result1)
    print("Expected: 5")
    print()
    root2 = build_tree([2, 2, 2])
    result2 = solution.findSecondMinimumValue(root2)
    print("Example 2:")
    print("Input:  root = [2,2,2]")
    print("Output:", result2)
    print("Expected: -1")
    print()
    root3 = build_tree([5])
    result3 = solution.findSecondMinimumValue(root3)
    print("Example 3 (extra):")
    print("Input:  root = [5]")
    print("Output:", result3)
    print("Expected: -1")
print(__name__)