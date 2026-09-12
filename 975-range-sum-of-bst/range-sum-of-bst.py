# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def rangeSumBST(self, root, low, high):
        """
        :type root: Optional[TreeNode]
        :type low: int
        :type high: int
        :rtype: int
        """
        if root is None:
            return 0
        if root.val < low:
            return self.rangeSumBST(root.right, low, high)
        if root.val > high:
            return self.rangeSumBST(root.left, low, high)
        return (
            root.val
            + self.rangeSumBST(root.left, low, high)
            + self.rangeSumBST(root.right, low, high)
        )
def build_tree(values):
    if not values or values[0] is None:
        return None
    nodes = [None if v is None else TreeNode(v) for v in values]
    kids = nodes[::-1]
    root = kids.pop()
    for node in nodes:
        if node:
            if kids:
                child = kids.pop()
                node.left = child
            if kids:
                child = kids.pop()
                node.right = child
    return root
if __name__ == "__main__":
    sol = Solution()
    root1 = build_tree([10, 5, 15, 3, 7, None, 18])
    print(sol.rangeSumBST(root1, 7, 15))  
    root2 = build_tree([10, 5, 15, 3, 7, 13, 18, 1, None, 6])
    print(sol.rangeSumBST(root2, 6, 10)) 
print(__name__)