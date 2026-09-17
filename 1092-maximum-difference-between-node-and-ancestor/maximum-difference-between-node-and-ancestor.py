# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def maxAncestorDiff(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        def dfs(node, current_min, current_max):
            if node is None:
                return current_max - current_min
            best_here = max(abs(node.val - current_min), abs(node.val - current_max))
            new_min = min(current_min, node.val)
            new_max = max(current_max, node.val)
            left_best = dfs(node.left, new_min, new_max)
            right_best = dfs(node.right, new_min, new_max)
            return max(best_here, left_best, right_best)
        return dfs(root, root.val, root.val)
def build_tree(values):
    if not values or values[0] is None:
        return None
    nodes = [None if v is None else TreeNode(v) for v in values]
    kid_index = 1
    for node in nodes:
        if node is None:
            continue
        if kid_index < len(nodes):
            node.left = nodes[kid_index]
            kid_index += 1
        if kid_index < len(nodes):
            node.right = nodes[kid_index]
            kid_index += 1
    return nodes[0]
if __name__ == "__main__":
    sol = Solution()
    test_cases = [
        ([8, 3, 10, 1, 6, None, 14, None, None, 4, 7, 13], 7),
        ([1, None, 2, None, 0, 3], 3),
        ([1, 2, 3], 2),
    ]
    for values, expected in test_cases:
        root = build_tree(values)
        result = sol.maxAncestorDiff(root)
        status = "PASS" if result == expected else "FAIL"
        print("root={0} -> {1} (expected {2}) [{3}]".format(
            values, result, expected, status
        ))
print(__name__)