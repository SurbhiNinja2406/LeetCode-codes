# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[Optional[TreeNode]]
        """
        if n == 0:
            return []
        memo = {}
        def build(start, end):
            if start > end:
                return [None] 
            if (start, end) in memo:
                return memo[(start, end)]
            all_trees = []
            for root_val in range(start, end + 1):
                left_subtrees = build(start, root_val - 1)
                right_subtrees = build(root_val + 1, end)
                for left in left_subtrees:
                    for right in right_subtrees:
                        root = TreeNode(root_val, left, right)
                        all_trees.append(root)
            memo[(start, end)] = all_trees
            return all_trees
        return build(1, n)
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
    trees3 = sol.generateTrees(3)
    print("n=3: {} trees".format(len(trees3)))
    for t in trees3:
        print(tree_to_list(t))
    trees1 = sol.generateTrees(1)
    print("n=1: {} trees".format(len(trees1)))
    for t in trees1:
        print(tree_to_list(t))
print()