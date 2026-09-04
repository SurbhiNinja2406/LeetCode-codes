# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def pruneTree(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: Optional[TreeNode]
        """
        if root is None:
            return None
        root.left = self.pruneTree(root.left)
        root.right = self.pruneTree(root.right)
        if root.val == 0 and root.left is None and root.right is None:
            return None
        return root
def build_tree(values):
    if not values or values[0] is None:
        return None
    root = TreeNode(values[0])
    queue = [root]
    i = 1
    n = len(values)
    while queue and i < n:
        node = queue.pop(0)
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
    if root is None:
        return []
    result = []
    queue = [root]
    while queue:
        node = queue.pop(0)
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
    test_cases = [
        ([1, None, 0, 0, 1], [1, None, 0, None, 1]),
        ([1, 0, 1, 0, 0, 0, 1], [1, None, 1, None, 1]),
        ([1, 1, 0, 1, 1, 0, 1, 0], [1, 1, 0, 1, None, 1]),
    ]
    for values, expected in test_cases:
        tree = build_tree(list(values))
        pruned = solution.pruneTree(tree)
        result = tree_to_list(pruned)
        status = "PASS" if result == expected else "FAIL"
        print("input={:<30} expected={:<20} got={:<20} [{}]".format(
            str(values), str(expected), str(result), status))
print(__name__)