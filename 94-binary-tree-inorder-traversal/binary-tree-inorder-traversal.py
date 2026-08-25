# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        result = []
        def traverse(node):
            if not node:
                return
            traverse(node.left)    
            result.append(node.val)  
            traverse(node.right)    
        traverse(root)
        return result
if __name__ == "__main__":
    sol = Solution()
    root1 = TreeNode(1, None, TreeNode(2, TreeNode(3)))
    print(sol.inorderTraversal(root1)) 
    root4 = TreeNode(1)
    print(sol.inorderTraversal(root4)) 
    print(sol.inorderTraversal(None)) 
print(__name__)