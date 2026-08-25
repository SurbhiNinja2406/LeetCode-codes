# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        result = []        
        def dfs(node):
            if not node:
                return            
            result.append(node.val)  
            dfs(node.left)           
            dfs(node.right)         
        dfs(root)
        return result
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
    root1 = build_tree([1, None, 2, 3])
    print(sol.preorderTraversal(root1)) 
    root2 = build_tree([1, 2, 3, 4, 5, None, 8, None, None, 6, 7, 9])
    print(sol.preorderTraversal(root2))  
    root3 = build_tree([])
    print(sol.preorderTraversal(root3)) 
    root4 = build_tree([1])
    print(sol.preorderTraversal(root4))
print(__name__)