# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sumNumbers(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        def dfs(node, current_number):
            if not node:
                return 0
            current_number = current_number * 10 + node.val
            if not node.left and not node.right:
                return current_number
            return dfs(node.left, current_number) + dfs(node.right, current_number)        
        return dfs(root, 0)
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
    print(sol.sumNumbers(root1)) 
    root2 = build_tree([4, 9, 0, 5, 1])
    print(sol.sumNumbers(root2)) 
print(__name__)