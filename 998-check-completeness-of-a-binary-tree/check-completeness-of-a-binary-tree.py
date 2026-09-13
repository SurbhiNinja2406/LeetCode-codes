# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def isCompleteTree(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        if not root:
            return True        
        queue = [root]
        seen_null = False        
        i = 0
        while i < len(queue):
            node = queue[i]
            i += 1            
            if node is None:
                seen_null = True
            else:
                if seen_null:
                    return False
                queue.append(node.left)
                queue.append(node.right)        
        return True
def build_tree(values):
    """
    Helper: build a binary tree from a LeetCode-style level-order list
    (using None for missing nodes) and return the root.
    """
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
    values1 = [1, 2, 3, 4, 5, 6]
    root1 = build_tree(values1)
    result1 = sol.isCompleteTree(root1)
    print("Input: root={}".format(values1))
    print("Output: {}".format(result1))
    print("Expected: True")
    print("Pass: {}\n".format(result1 == True))
    values2 = [1, 2, 3, 4, 5, None, 7]
    root2 = build_tree(values2)
    result2 = sol.isCompleteTree(root2)
    print("Input: root={}".format(values2))
    print("Output: {}".format(result2))
    print("Expected: False")
    print("Pass: {}\n".format(result2 == False))
    values3 = [1]
    root3 = build_tree(values3)
    result3 = sol.isCompleteTree(root3)
    print("Input: root={}".format(values3))
    print("Output: {}".format(result3))
    print("Expected: True")
    print("Pass: {}\n".format(result3 == True))
    values4 = [1, None, 2]
    root4 = build_tree(values4)
    result4 = sol.isCompleteTree(root4)
    print("Input: root={}".format(values4))
    print("Output: {}".format(result4))
    print("Expected: False")
    print("Pass: {}\n".format(result4 == False))
    values5 = [1, 2, 3, 4, 5, 6, 7]
    root5 = build_tree(values5)
    result5 = sol.isCompleteTree(root5)
    print("Input: root={}".format(values5))
    print("Output: {}".format(result5))
    print("Expected: True")
    print("Pass: {}\n".format(result5 == True))
    values6 = [1, 2, 3, 4, None, 6, 7]
    root6 = build_tree(values6)
    result6 = sol.isCompleteTree(root6)
    print("Input: root={}".format(values6))
    print("Output: {}".format(result6))
    print("Expected: False")
    print("Pass: {}\n".format(result6 == False))
print(__name__)