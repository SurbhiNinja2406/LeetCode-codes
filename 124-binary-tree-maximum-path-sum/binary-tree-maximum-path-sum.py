# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxPathSum(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        self.max_sum = float('-inf')        
        def max_gain(node):
            if not node:
                return 0
            left_gain = max(max_gain(node.left), 0)
            right_gain = max(max_gain(node.right), 0)
            price_new_path = node.val + left_gain + right_gain
            self.max_sum = max(self.max_sum, price_new_path)
            return node.val + max(left_gain, right_gain)        
        max_gain(root)
        return self.max_sum
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
    root1 = build_tree([1, 2, 3])
    print(sol.maxPathSum(root1)) 
    root2 = build_tree([-10, 9, 20, None, None, 15, 7])
    print(sol.maxPathSum(root2)) 
print(__name__)