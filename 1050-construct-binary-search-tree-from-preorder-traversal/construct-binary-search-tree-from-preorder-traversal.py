# Definition for a binary tree node.
'''
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
'''
class Solution(object):
    def bstFromPreorder(self, preorder):
        """
        :type preorder: List[int]
        :rtype: Optional[TreeNode]
        """
        self.index = 0
        n = len(preorder)
        def build(bound):
            if self.index == n or preorder[self.index] > bound:
                return None
            root_val = preorder[self.index]
            self.index += 1
            root = TreeNode(root_val)
            root.left = build(root_val)
            root.right = build(bound)
            return root
        return build(float('inf'))
def tree_to_level_order(root):
    if root is None:
        return []
    result = []
    queue = [root]
    while queue:
        node = queue.pop(0)
        if node is None:
            result.append(None)
        else:
            result.append(node.val)
            queue.append(node.left)
            queue.append(node.right)
    while result and result[-1] is None:
        result.pop()
    return result
def format_list(lst):
    parts = []
    for item in lst:
        if item is None:
            parts.append("null")
        else:
            parts.append(str(item))
    return "[" + ",".join(parts) + "]"
if __name__ == "__main__":
    solution = Solution()
    preorder1 = [8, 5, 1, 7, 10, 12]
    root1 = solution.bstFromPreorder(preorder1)
    output1 = tree_to_level_order(root1)
    print("Example 1: preorder={}".format(preorder1))
    print("Output: {}".format(format_list(output1)))
    print("Expected: [8,5,10,1,7,null,12]")
    print("")
    preorder2 = [1, 3]
    root2 = solution.bstFromPreorder(preorder2)
    output2 = tree_to_level_order(root2)
    print("Example 2: preorder={}".format(preorder2))
    print("Output: {}".format(format_list(output2)))
    print("Expected: [1,null,3]")
    print("")
    preorder3 = [5]
    root3 = solution.bstFromPreorder(preorder3)
    output3 = tree_to_level_order(root3)
    print("Example 3: preorder={}".format(preorder3))
    print("Output: {}".format(format_list(output3)))
    print("Expected: [5]")
    print("")
    preorder4 = [10, 8, 6, 4]
    root4 = solution.bstFromPreorder(preorder4)
    output4 = tree_to_level_order(root4)
    print("Example 4: preorder={}".format(preorder4))
    print("Output: {}".format(format_list(output4)))
    print("Expected: [10,8,null,6,null,4]")
print(__name__)