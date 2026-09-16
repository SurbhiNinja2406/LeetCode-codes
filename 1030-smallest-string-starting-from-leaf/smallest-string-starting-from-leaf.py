# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def smallestFromLeaf(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: str
        """
        self.best = None
        def dfs(node, path):
            if not node:
                return
            char = chr(ord('a') + node.val)
            path = char + path
            if not node.left and not node.right:
                if self.best is None or path < self.best:
                    self.best = path
                return
            dfs(node.left, path)
            dfs(node.right, path)
        dfs(root, "")
        return self.best
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
    root1 = build_tree([0, 1, 2, 3, 4, 3, 4])
    print(sol.smallestFromLeaf(root1))  
    root2 = build_tree([25, 1, 3, 1, 3, 0, 2])
    print(sol.smallestFromLeaf(root2))  
    root3 = build_tree([2, 2, 1, None, 1, 0, None, 0])
    print(sol.smallestFromLeaf(root3)) 