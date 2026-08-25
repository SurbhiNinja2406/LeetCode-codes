# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: Optional[TreeNode]
        """
        inorder_index = {val: idx for idx, val in enumerate(inorder)}
        self.pre_idx = 0 
        def build(left, right):
            if left > right:
                return None
            root_val = preorder[self.pre_idx]
            self.pre_idx += 1
            root = TreeNode(root_val)
            mid = inorder_index[root_val]
            root.left = build(left, mid - 1)
            root.right = build(mid + 1, right)
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
    root1 = sol.buildTree([3, 9, 20, 15, 7], [9, 3, 15, 20, 7])
    print("Test 1: {}".format(tree_to_list(root1)))  
    root2 = sol.buildTree([-1], [-1])
    print("Test 2: {}".format(tree_to_list(root2))) 
print(__name__)