# Definition for a binary tree node.
from collections import defaultdict


class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def verticalTraversal(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[List[int]]
        """
        nodes = []
        def dfs(node, row, col):
            if not node:
                return
            nodes.append((col, row, node.val))
            dfs(node.left, row + 1, col - 1)
            dfs(node.right, row + 1, col + 1)
        dfs(root, 0, 0)
        nodes.sort(key=lambda x: (x[0], x[1], x[2]))
        columns = defaultdict(list)
        for col, row, val in nodes:
            columns[col].append(val)
        min_col = min(columns.keys())
        max_col = max(columns.keys())
        return [columns[c] for c in range(min_col, max_col + 1)]
def build_tree(values):
    if not values or values[0] is None:
        return None
    nodes = [None if v is None else TreeNode(v) for v in values]
    kids = nodes[::-1]
    root = kids.pop()
    for node in nodes:
        if node:
            if kids:
                node.left = kids.pop()
            if kids:
                node.right = kids.pop()
    return root
if __name__ == "__main__":
    sol = Solution()
    root1 = build_tree([3, 9, 20, None, None, 15, 7])
    print(sol.verticalTraversal(root1))  
    root2 = build_tree([1, 2, 3, 4, 5, 6, 7])
    print(sol.verticalTraversal(root2))  
    root3 = build_tree([1, 2, 3, 4, 6, 5, 7])
    print(sol.verticalTraversal(root3)) 