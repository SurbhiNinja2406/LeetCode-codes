# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: Optional[TreeNode]
        """
        inorder_index = {val: idx for idx, val in enumerate(inorder)}
        self.post_idx = len(postorder) - 1  
        def build(left, right):
            if left > right:
                return None
            root_val = postorder[self.post_idx]
            self.post_idx -= 1
            root = TreeNode(root_val)
            mid = inorder_index[root_val]
            root.right = build(mid + 1, right)
            root.left = build(left, mid - 1)
            return root
        return build(0, len(inorder) - 1)
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
    root1 = sol.buildTree([9, 3, 15, 20, 7], [9, 15, 7, 20, 3])
    print("Test 1: {}".format(tree_to_list(root1)))
    root2 = sol.buildTree([-1], [-1])
    print("Test 2: {}".format(tree_to_list(root2))) 
print(__name__)