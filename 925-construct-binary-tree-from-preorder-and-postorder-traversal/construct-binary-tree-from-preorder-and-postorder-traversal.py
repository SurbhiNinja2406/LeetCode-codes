# Definition for a binary tree node.
'''
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
'''
class Solution(object):
    def constructFromPrePost(self, preorder, postorder):
        """
        :type preorder: List[int]
        :type postorder: List[int]
        :rtype: Optional[TreeNode]
        """
        post_index = {val: i for i, val in enumerate(postorder)}
        def build(pre_left, pre_right, post_left, post_right):
            if pre_left > pre_right:
                return None
            root_val = preorder[pre_left]
            root = TreeNode(root_val)
            if pre_left == pre_right:
                return root
            left_root_val = preorder[pre_left + 1]
            left_subtree_size = post_index[left_root_val] - post_left + 1
            root.left = build(
                pre_left + 1, pre_left + left_subtree_size,
                post_left, post_left + left_subtree_size - 1
            )
            root.right = build(
                pre_left + left_subtree_size + 1, pre_right,
                post_left + left_subtree_size, post_right - 1
            )
            return root
        return build(0, len(preorder) - 1, 0, len(postorder) - 1)
def tree_to_preorder_list(root):
    if root is None:
        return []
    result = [root.val]
    result += tree_to_preorder_list(root.left)
    result += tree_to_preorder_list(root.right)
    return result
if __name__ == "__main__":
    sol = Solution()
    preorder1 = [1, 2, 4, 5, 3, 6, 7]
    postorder1 = [4, 5, 2, 6, 7, 3, 1]
    root1 = sol.constructFromPrePost(preorder1, postorder1)
    print("Example 1 preorder of result: {} (expected [1,2,3,4,5,6,7] preorder)".format(
        tree_to_preorder_list(root1)
    ))
    preorder2 = [1]
    postorder2 = [1]
    root2 = sol.constructFromPrePost(preorder2, postorder2)
    print("Example 2 preorder of result: {} (expected [1])".format(
        tree_to_preorder_list(root2)
    ))
print(__name__)