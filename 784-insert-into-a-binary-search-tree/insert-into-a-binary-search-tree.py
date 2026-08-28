# Definition for a binary tree node.
'''
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
'''
class Solution(object):
    def insertIntoBST(self, root, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode
        """
        if root is None:
            return TreeNode(val)
        curr = root
        while True:
            if val < curr.val:
                if curr.left is None:
                    curr.left = TreeNode(val)
                    break
                curr = curr.left
            else: 
                if curr.right is None:
                    curr.right = TreeNode(val)
                    break
                curr = curr.right
        return root
from collections import deque
def build_bst(values):
    if not values or values[0] is None:
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
def tree_to_level_order(root):
    if root is None:
        return []
    result = []
    queue = deque([root])
    while queue:
        node = queue.popleft()
        if node is None:
            result.append(None)
            continue
        result.append(node.val)
        queue.append(node.left)
        queue.append(node.right)
    while result and result[-1] is None:
        result.pop()
    return result
if __name__ == "__main__":
    sol = Solution()
    root1 = build_bst([4, 2, 7, 1, 3])
    result1 = sol.insertIntoBST(root1, 5)
    print(tree_to_level_order(result1)) 
    root2 = build_bst([40, 20, 60, 10, 30, 50, 70])
    result2 = sol.insertIntoBST(root2, 25)
    print(tree_to_level_order(result2))  
    root3 = build_bst([4, 2, 7, 1, 3])
    result3 = sol.insertIntoBST(root3, 5)
    print(tree_to_level_order(result3)) 
print(__name__)