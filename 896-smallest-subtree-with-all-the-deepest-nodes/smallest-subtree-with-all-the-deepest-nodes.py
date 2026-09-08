# Definition for a binary tree node.
# class TreeNode(object):
from collections import deque
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def subtreeWithAllDeepest(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: Optional[TreeNode]
        """
        def dfs(node):
            if not node:
                return (None, 0)            
            left_node, left_depth = dfs(node.left)
            right_node, right_depth = dfs(node.right)            
            if left_depth == right_depth:
                return (node, left_depth + 1)
            elif left_depth > right_depth:
                return (left_node, left_depth + 1)
            else:
                return (right_node, right_depth + 1)        
        result_node, _ = dfs(root)
        return result_node
def build_tree(values):
    if not values or values[0] is None:
        return None
    root = TreeNode(values[0])
    queue = deque([root])
    i = 1
    n = len(values)
    while queue and i < n:
        node = queue.popleft()
        if i < n:
            left_val = values[i]
            i += 1
            if left_val is not None:
                node.left = TreeNode(left_val)
                queue.append(node.left)
        if i < n:
            right_val = values[i]
            i += 1
            if right_val is not None:
                node.right = TreeNode(right_val)
                queue.append(node.right)
    return root
def tree_to_list(root):
    if not root:
        return []
    result = []
    queue = deque([root])
    while queue:
        node = queue.popleft()
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
    values1 = [3, 5, 1, 6, 2, 0, 8, None, None, 7, 4]
    root1 = build_tree(values1)
    result1 = sol.subtreeWithAllDeepest(root1)
    print("Example 1:")
    print("Input: root = {}".format(values1))
    print("Output:", tree_to_list(result1))
    print("Expected: [2, 7, 4]")
    print()
    values2 = [1]
    root2 = build_tree(values2)
    result2 = sol.subtreeWithAllDeepest(root2)
    print("Example 2:")
    print("Input: root = {}".format(values2))
    print("Output:", tree_to_list(result2))
    print("Expected: [1]")
    print()
    values3 = [0, 1, 3, None, 2]
    root3 = build_tree(values3)
    result3 = sol.subtreeWithAllDeepest(root3)
    print("Example 3:")
    print("Input: root = {}".format(values3))
    print("Output:", tree_to_list(result3))
    print("Expected: [2]")
print(__name__)