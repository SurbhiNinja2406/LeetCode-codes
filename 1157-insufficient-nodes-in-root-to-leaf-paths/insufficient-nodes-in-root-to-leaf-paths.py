# Definition for a binary tree node.
import sys
from collections import deque
sys.setrecursionlimit(10000)  
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def sufficientSubset(self, root, limit):
        """
        :type root: Optional[TreeNode]
        :type limit: int
        :rtype: Optional[TreeNode]
        """
        def dfs(node, path_sum):
            if not node:
                return None
            path_sum += node.val
            if not node.left and not node.right:
                return node if path_sum >= limit else None
            node.left = dfs(node.left, path_sum)
            node.right = dfs(node.right, path_sum)
            if not node.left and not node.right:
                return None
            return node
        return dfs(root, 0)
def build_tree(values):
    if not values:
        return None
    root = TreeNode(values[0])
    queue = deque([root])
    i = 1
    while queue and i < len(values):
        node = queue.popleft()
        if i < len(values) and values[i] is not None:
            node.left = TreeNode(values[i])
            queue.append(node.left)
        i += 1
        if i < len(values) and values[i] is not None:
            node.right = TreeNode(values[i])
            queue.append(node.right)
        i += 1
    return root
def to_list(root):
    if not root:
        return []
    out = []
    queue = deque([root])
    while queue:
        node = queue.popleft()
        if node:
            out.append(node.val)
            queue.append(node.left)
            queue.append(node.right)
        else:
            out.append(None)
    while out and out[-1] is None:
        out.pop()
    return out
if __name__ == "__main__":
    sol = Solution()
    tests = [
        ([1, 2, 3, 4, -99, -99, 7, 8, 9, -99, -99, 12, 13, -99, 14], 1),
        ([5, 4, 8, 11, None, 17, 4, 7, 1, None, None, 5, 3], 22),
        ([1, 2, -3, -5, None, 4, None], -1),
    ]
    for values, limit in tests:
        result = sol.sufficientSubset(build_tree(values), limit)
        print("limit = {} -> {}".format(limit, to_list(result)))
print(__name__)