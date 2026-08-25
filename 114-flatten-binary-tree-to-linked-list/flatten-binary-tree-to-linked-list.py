# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def flatten(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: None Do not return anything, modify root in-place instead.
        """
        self.prev = None 
        def reverse_preorder(node):
            if node is None:
                return
            reverse_preorder(node.right)
            reverse_preorder(node.left)
            node.right = self.prev
            node.left = None
            self.prev = node
        reverse_preorder(root)
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
def flattened_to_list(root):
    result = []
    node = root
    while node:
        result.append(node.val)
        result.append(None) 
        node = node.right
    return result
if __name__ == "__main__":
    sol = Solution()
    root1 = build_tree([1, 2, 5, 3, 4, None, 6])
    sol.flatten(root1)
    print("Test 1: {}".format(flattened_to_list(root1)))
    root2 = build_tree([])
    sol.flatten(root2)
    print("Test 2: {}".format(flattened_to_list(root2))) 
    root3 = build_tree([0])
    sol.flatten(root3)
    print("Test 3: {}".format(flattened_to_list(root3)))