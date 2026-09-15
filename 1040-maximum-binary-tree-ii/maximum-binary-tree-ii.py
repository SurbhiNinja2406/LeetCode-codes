# Definition for a binary tree node.
'''
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
'''
class Solution(object):
    def insertIntoMaxTree(self, root, val):
        """
        :type root: Optional[TreeNode]
        :type val: int
        :rtype: Optional[TreeNode]
        """
        if root is None or val > root.val:
            new_node = TreeNode(val)
            new_node.left = root
            return new_node
        root.right = self.insertIntoMaxTree(root.right, val)
        return root
def build_tree(values):
    if not values or values[0] is None:
        return None
    nodes = [None if v is None else TreeNode(v) for v in values]
    kids = nodes[::-1]
    root = kids.pop()
    for node in nodes:
        if node:
            if kids:
                child = kids.pop()
                node.left = child
            if kids:
                child = kids.pop()
                node.right = child
    return root
def tree_to_level_order(root):
    if not root:
        return []
    result = []
    queue = [root]
    while queue:
        node = queue.pop(0)
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
    root1 = build_tree([4, 1, 3, None, None, 2])
    result1 = sol.insertIntoMaxTree(root1, 5)
    print(tree_to_level_order(result1))  
    root2 = build_tree([5, 2, 4, None, 1])
    result2 = sol.insertIntoMaxTree(root2, 3)
    print(tree_to_level_order(result2)) 
    root3 = build_tree([5, 2, 3, None, 1])
    result3 = sol.insertIntoMaxTree(root3, 4)
    print(tree_to_level_order(result3))  
print(__name__)