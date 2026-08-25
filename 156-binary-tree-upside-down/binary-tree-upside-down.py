from collections import deque
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def upsideDownBinaryTree(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: Optional[TreeNode]
        """
        if root is None or root.left is None:
            return root
        new_root = self.upsideDownBinaryTree(root.left)
        root.left.left = root.right
        root.left.right = root
        root.left = None
        root.right = None
        return new_root
def build_tree(values):
    """Build a binary tree from a level-order list (LeetCode style, with None for missing nodes)."""
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
def tree_to_list(root):
    """Convert a binary tree to a level-order list (LeetCode style), trimming trailing Nones."""
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
    test_cases = [
        [1, 2, 3, 4, 5],
        [],
        [1],
    ]
    solution = Solution()
    for values in test_cases:
        root = build_tree(values)
        new_root = solution.upsideDownBinaryTree(root)
        output = tree_to_list(new_root)
        print("Input:  root = {}".format(values))
        print("Output: {}".format(output))
        print("")
print(__name__)