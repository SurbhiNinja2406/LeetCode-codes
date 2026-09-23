# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def btreeGameWinningMove(self, root, n, x):
        """
        :type root: Optional[TreeNode]
        :type n: int
        :type x: int
        :rtype: bool
        """
        self.left_size = 0
        self.right_size = 0
        def count_nodes(node):
            if not node:
                return 0
            left_count = count_nodes(node.left)
            right_count = count_nodes(node.right)
            if node.val == x:
                self.left_size = left_count
                self.right_size = right_count
            return left_count + right_count + 1
        count_nodes(root)
        parent_size = n - self.left_size - self.right_size - 1
        half = n // 2
        return (self.left_size > half or
                self.right_size > half or
                parent_size > half)
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
    root1 = build_tree([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11])
    print(sol.btreeGameWinningMove(root1, 11, 3))  
    root2 = build_tree([1, 2, 3])
    print(sol.btreeGameWinningMove(root2, 3, 1))   