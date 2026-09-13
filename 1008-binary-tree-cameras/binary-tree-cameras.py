# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def minCameraCover(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        self.cameras = 0
        NOT_COVERED = 0
        COVERED_NO_CAMERA = 1
        HAS_CAMERA = 2        
        def dfs(node):
            if not node:
                return COVERED_NO_CAMERA            
            left_state = dfs(node.left)
            right_state = dfs(node.right)            
            if left_state == NOT_COVERED or right_state == NOT_COVERED:
                self.cameras += 1
                return HAS_CAMERA            
            if left_state == HAS_CAMERA or right_state == HAS_CAMERA:
                return COVERED_NO_CAMERA            
            return NOT_COVERED        
        root_state = dfs(root)        
        if root_state == NOT_COVERED:
            self.cameras += 1        
        return self.cameras
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
    values1 = [0, 0, None, 0, 0]
    root1 = build_tree(values1)
    result1 = sol.minCameraCover(root1)
    print("Input: root={}".format(values1))
    print("Output: {}".format(result1))
    print("Expected: 1")
    print("Pass: {}\n".format(result1 == 1))
    values2 = [0, 0, None, 0, None, 0, None, None, 0]
    root2 = build_tree(values2)
    result2 = sol.minCameraCover(root2)
    print("Input: root={}".format(values2))
    print("Output: {}".format(result2))
    print("Expected: 2")
    print("Pass: {}\n".format(result2 == 2))
    values3 = [0]
    root3 = build_tree(values3)
    result3 = sol.minCameraCover(root3)
    print("Input: root={}".format(values3))
    print("Output: {}".format(result3))
    print("Expected: 1")
    print("Pass: {}\n".format(result3 == 1))
    values4 = [0, 0]
    root4 = build_tree(values4)
    result4 = sol.minCameraCover(root4)
    print("Input: root={}".format(values4))
    print("Output: {}".format(result4))
    print("Expected: 1")
    print("Pass: {}\n".format(result4 == 1))
    values5 = [0, 0, 0, 0, 0, 0, 0]
    root5 = build_tree(values5)
    result5 = sol.minCameraCover(root5)
    print("Input: root={}".format(values5))
    print("Output: {}".format(result5))
    print("Expected: 1")
    print("Pass: {}\n".format(result5 == 1))
    values6 = [0, 0, None, 0, None, 0, None, 0, None, 0]
    root6 = build_tree(values6)
    result6 = sol.minCameraCover(root6)
    print("Input: root={}".format(values6))
    print("Output: {}".format(result6))
print(__name__)