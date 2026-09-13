# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def isUnivalTree(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        if not root:
            return True        
        root_val = root.val        
        def dfs(node):
            if not node:
                return True
            if node.val != root_val:
                return False
            return dfs(node.left) and dfs(node.right)
        return dfs(root)
def build_tree(values):
    if not values or values[0] is None:
        return None    
    root = TreeNode(values[0])
    queue = [root]
    i = 1    
    while queue and i < len(values):
        node = queue.pop(0)        
        if i < len(values):
            left_val = values[i]
            i += 1
            if left_val is not None:
                node.left = TreeNode(left_val)
                queue.append(node.left)        
        if i < len(values):
            right_val = values[i]
            i += 1
            if right_val is not None:
                node.right = TreeNode(right_val)
                queue.append(node.right)    
    return root
if __name__ == "__main__":
    sol = Solution()
    values1 = [1, 1, 1, 1, 1, None, 1]
    root1 = build_tree(values1)
    result1 = sol.isUnivalTree(root1)
    print("Input: root={}".format(values1))
    print("Output: {}".format(result1))
    print("Expected: True")
    print("Pass: {}\n".format(result1 == True))
    values2 = [2, 2, 2, 5, 2]
    root2 = build_tree(values2)
    result2 = sol.isUnivalTree(root2)
    print("Input: root={}".format(values2))
    print("Output: {}".format(result2))
    print("Expected: False")
    print("Pass: {}\n".format(result2 == False))
    values3 = [5]
    root3 = build_tree(values3)
    result3 = sol.isUnivalTree(root3)
    print("Input: root={}".format(values3))
    print("Output: {}".format(result3))
    print("Expected: True")
    print("Pass: {}\n".format(result3 == True))
    values4 = [0, 0, 0]
    root4 = build_tree(values4)
    result4 = sol.isUnivalTree(root4)
    print("Input: root={}".format(values4))
    print("Output: {}".format(result4))
    print("Expected: True")
    print("Pass: {}\n".format(result4 == True))
    values5 = [3, 3, None, 3, None, None, None, 3]
    root5 = build_tree(values5)
    result5 = sol.isUnivalTree(root5)
    print("Input: root={}".format(values5))
    print("Output: {}".format(result5))
    print("Expected: True")
    print("Pass: {}\n".format(result5 == True))
    values6 = [7, 7, 7, 7, 7, 7, 8]
    root6 = build_tree(values6)
    result6 = sol.isUnivalTree(root6)
    print("Input: root={}".format(values6))
    print("Output: {}".format(result6))
    print("Expected: False")
    print("Pass: {}\n".format(result6 == False))
print(__name__)