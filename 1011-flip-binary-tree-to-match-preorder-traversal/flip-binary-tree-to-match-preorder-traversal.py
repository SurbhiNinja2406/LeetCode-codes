# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def flipMatchVoyage(self, root, voyage):
        """
        :type root: Optional[TreeNode]
        :type voyage: List[int]
        :rtype: List[int]
        """
        self.idx = 0
        self.flipped = []
        self.possible = True
        def dfs(node):
            if not node or not self.possible:
                return
            if node.val != voyage[self.idx]:
                self.possible = False
                return
            self.idx += 1
            if node.left and self.idx < len(voyage) and node.left.val != voyage[self.idx]:
                self.flipped.append(node.val)
                dfs(node.right)
                dfs(node.left)
            else:
                dfs(node.left)
                dfs(node.right)
        dfs(root)
        return self.flipped if self.possible else [-1]
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
    root1 = build_tree([1, 2])
    print(sol.flipMatchVoyage(root1, [2, 1])) 
    root2 = build_tree([1, 2, 3])
    print(sol.flipMatchVoyage(root2, [1, 3, 2])) 
    root3 = build_tree([1, 2, 3])
    print(sol.flipMatchVoyage(root3, [1, 2, 3])) 
print(__name__)