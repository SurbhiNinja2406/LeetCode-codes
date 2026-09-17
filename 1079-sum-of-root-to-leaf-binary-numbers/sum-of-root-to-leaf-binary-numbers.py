# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def sumRootToLeaf(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        def dfs(node, current_value):
            if node is None:
                return 0
            current_value = current_value * 2 + node.val
            if node.left is None and node.right is None:
                return current_value
            return dfs(node.left, current_value) + dfs(node.right, current_value)
        return dfs(root, 0)
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
        ([1, 0, 1, 0, 1, 0, 1], 22),
        ([0], 0),
        ([1], 1),
        ([1, 1], 3),
    ]
    for values, expected in test_cases:
        root = build_tree(values)
        result = sol.sumRootToLeaf(root)
        status = "PASS" if result == expected else "FAIL"
        print("root={0} -> {1} (expected {2}) [{3}]".format(
            values, result, expected, status
        ))
print(__name__)