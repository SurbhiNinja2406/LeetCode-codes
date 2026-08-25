# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def hasPathSum(self, root, targetSum):
        """
        :type root: Optional[TreeNode]
        :type targetSum: int
        :rtype: bool
        """
        if root is None:
            return False 
        remaining = targetSum - root.val
        if root.left is None and root.right is None:
            return remaining == 0
        return (self.hasPathSum(root.left, remaining) or
                self.hasPathSum(root.right, remaining))
def build_tree(values):
    if not values or values[0] is None:
        return None
    root = TreeNode(values[0])
    queue = [root]
    i = 1
    while queue and i < len(values):
        node = queue.pop(0)
        if i < len(values):
            if values[i] is not None:
                node.left = TreeNode(values[i])
                queue.append(node.left)
            i += 1
        if i < len(values):
            if values[i] is not None:
                node.right = TreeNode(values[i])
                queue.append(node.right)
            i += 1
    return root
if __name__ == "__main__":
    sol = Solution()
    root1 = build_tree([5, 4, 8, 11, None, 13, 4, 7, 2, None, None, None, 1])
    print("Test 1: {}".format(sol.hasPathSum(root1, 22)))
    root2 = build_tree([1, 2, 3])
    print("Test 2: {}".format(sol.hasPathSum(root2, 5)))
    root3 = build_tree([])
    print("Test 3: {}".format(sol.hasPathSum(root3, 0)))
print(__name__)