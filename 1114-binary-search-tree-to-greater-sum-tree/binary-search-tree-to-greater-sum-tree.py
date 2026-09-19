# Definition for a binary tree node.
from collections import deque
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def bstToGst(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: Optional[TreeNode]
        """
        total = 0
        stack = []
        node = root
        while stack or node:
            while node:
                stack.append(node)
                node = node.right      
            node = stack.pop()
            total += node.val          
            node.val = total        
            node = node.left         
        return root
def build_tree(values):
    if not values:
        return None
    root = TreeNode(values[0])
    queue = deque([root])
    i = 1
    while queue and i < len(values):
        node = queue.popleft()
        if i < len(values) and values[i] is not None:
            node.left = TreeNode(values[i])
            queue.append(node.left)
        i += 1
        if i < len(values) and values[i] is not None:
            node.right = TreeNode(values[i])
            queue.append(node.right)
        i += 1
    return root
def serialize(root):
    if not root:
        return []
    result = []
    queue = deque([root])
    while queue:
        node = queue.popleft()
        if node:
            result.append(node.val)
            queue.append(node.left)
            queue.append(node.right)
        else:
            result.append(None)
    while result and result[-1] is None:  
        result.pop()
    return result
if __name__ == "__main__":
    sol = Solution()
    tests = [
        ([4, 1, 6, 0, 2, 5, 7, None, None, None, 3, None, None, None, 8],
         [30, 36, 21, 36, 35, 26, 15, None, None, None, 33, None, None, None, 8]),
        ([0, None, 1], [1, None, 1]),
    ]
    for values, expected in tests:
        result = serialize(sol.bstToGst(build_tree(values)))
        status = "PASS" if result == expected else "FAIL"
        print("{}: got {}, expected {}".format(status, result, expected))
print(__name__)