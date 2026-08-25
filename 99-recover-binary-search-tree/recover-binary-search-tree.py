# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def recoverTree(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: None Do not return anything, modify root in-place instead.
        """
        self.first = None
        self.second = None
        self.prev = None
        def inorder(node):
            if node is None:
                return
            inorder(node.left)
            if self.prev is not None and self.prev.val > node.val:
                if self.first is None:
                    self.first = self.prev
                self.second = node
            self.prev = node
            inorder(node.right)
        inorder(root)
        if self.first and self.second:
            self.first.val, self.second.val = self.second.val, self.first.val
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
def tree_to_list(root):
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
    root1 = build_tree([1, 3, None, None, 2])
    sol.recoverTree(root1)
    print("Test 1: {}".format(tree_to_list(root1)))
    root2 = build_tree([3, 1, 4, None, None, 2])
    sol.recoverTree(root2)
    print("Test 2: {}".format(tree_to_list(root2)))  
print(__name__)