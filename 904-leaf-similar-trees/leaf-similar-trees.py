# Definition for a binary tree node.
from collections import deque
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def leafSimilar(self, root1, root2):
        """
        :type root1: Optional[TreeNode]
        :type root2: Optional[TreeNode]
        :rtype: bool
        """        
        def get_leaf_sequence(node):
            leaves = []
            def dfs(n):
                if not n:
                    return
                if not n.left and not n.right:
                    leaves.append(n.val)
                    return
                dfs(n.left)
                dfs(n.right)            
            dfs(node)
            return leaves
        return get_leaf_sequence(root1) == get_leaf_sequence(root2)
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
if __name__ == "__main__":
    sol = Solution()
    values1_1 = [3, 5, 1, 6, 2, 9, 8, None, None, 7, 4]
    values1_2 = [3, 5, 1, 6, 7, 4, 2, None, None, None, None, None, None, 9, 8]
    root1_1 = build_tree(values1_1)
    root1_2 = build_tree(values1_2)
    result1 = sol.leafSimilar(root1_1, root1_2)
    print("Example 1:")
    print("Input: root1 = {}, root2 = {}".format(values1_1, values1_2))
    print("Output:", result1)
    print("Expected: True")
    print()
    values2_1 = [1, 2, 3]
    values2_2 = [1, 3, 2]
    root2_1 = build_tree(values2_1)
    root2_2 = build_tree(values2_2)
    result2 = sol.leafSimilar(root2_1, root2_2)
    print("Example 2:")
    print("Input: root1 = {}, root2 = {}".format(values2_1, values2_2))
    print("Output:", result2)
    print("Expected: False")
    print()
    values3_1 = [5]
    values3_2 = [5]
    root3_1 = build_tree(values3_1)
    root3_2 = build_tree(values3_2)
    result3 = sol.leafSimilar(root3_1, root3_2)
    print("Additional test (single node, same value):")
    print("Input: root1 = {}, root2 = {}".format(values3_1, values3_2))
    print("Output:", result3)
    print("Expected: True")
print(__name__)