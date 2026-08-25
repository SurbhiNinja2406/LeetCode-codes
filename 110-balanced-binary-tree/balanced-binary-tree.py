# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isBalanced(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        def check_height(node):
            if node is None:
                return 0
            left_height = check_height(node.left)
            if left_height == -1:
                return -1  
            right_height = check_height(node.right)
            if right_height == -1:
                return -1 
            if abs(left_height - right_height) > 1:
                return -1  
            return 1 + max(left_height, right_height)
        return check_height(root) != -1
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
    root1 = build_tree([3, 9, 20, None, None, 15, 7])
    print("Test 1: {}".format(sol.isBalanced(root1))) 
    root2 = build_tree([1, 2, 2, 3, 3, None, None, 4, 4])
    print("Test 2: {}".format(sol.isBalanced(root2))) 
    root3 = build_tree([])
    print("Test 3: {}".format(sol.isBalanced(root3))) 
print(__name__)