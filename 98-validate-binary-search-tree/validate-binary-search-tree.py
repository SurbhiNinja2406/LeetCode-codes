# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isValidBST(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        def validate(node, low, high):
            if node is None:
                return True
            # Node's value must be strictly within (low, high)
            if low is not None and node.val <= low:
                return False
            if high is not None and node.val >= high:
                return False
            return (validate(node.left, low, node.val) and
                    validate(node.right, node.val, high))
        return validate(root, None, None)
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
    root1 = build_tree([2, 1, 3])
    print("Test 1: {}".format(sol.isValidBST(root1)))  
    root2 = build_tree([5, 1, 4, None, None, 3, 6])
    print("Test 2: {}".format(sol.isValidBST(root2))) 
    root3 = build_tree([1])
    print("Test 3: {}".format(sol.isValidBST(root3)))  
    root4 = build_tree([5, 4, 6, None, None, 3, 7])
    print("Test 4: {}".format(sol.isValidBST(root4)))
print(__name__)