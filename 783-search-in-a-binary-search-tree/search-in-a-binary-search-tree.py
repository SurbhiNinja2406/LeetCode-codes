# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def searchBST(self, root, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode
        """
        curr = root
        while curr is not None:
            if val == curr.val:
                return curr
            elif val < curr.val:
                curr = curr.left
            else:
                curr = curr.right
        return None  
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
def tree_to_list(root):
    if root is None:
        return []
    result = [root.val]
    result += tree_to_list(root.left)
    result += tree_to_list(root.right)
    return result
if __name__ == "__main__":
    sol = Solution()
    root = build_bst([4, 2, 7, 1, 3])
    found = sol.searchBST(root, 2)
    print(tree_to_list(found) if found else [])  
    found2 = sol.searchBST(root, 5)
    print(tree_to_list(found2) if found2 else [])  
print(__name__)