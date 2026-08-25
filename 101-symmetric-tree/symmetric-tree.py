# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        if root is None:
            return True
        def is_mirror(left, right):
            if left is None and right is None:
                return True
            if left is None or right is None:
                return False
            if left.val != right.val:
                return False
            return (is_mirror(left.left, right.right) and
                    is_mirror(left.right, right.left))
        return is_mirror(root.left, root.right)
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
    root1 = build_tree([1, 2, 2, 3, 4, 4, 3])
    print("Test 1: {}".format(sol.isSymmetric(root1)))  
    root2 = build_tree([1, 2, 2, None, 3, None, 3])
    print("Test 2: {}".format(sol.isSymmetric(root2)))
print(__name__)