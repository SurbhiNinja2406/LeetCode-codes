# Definition for a binary tree node.
'''
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
'''
class Solution(object):
    def allPossibleFBT(self, n):
        """
        :type n: int
        :rtype: List[Optional[TreeNode]]
        """
        memo = {}
        def build(n):
            if n % 2 == 0:
                return []
            if n == 1:
                return [TreeNode(0)]
            if n in memo:
                return memo[n]
            result = []
            for left_size in range(1, n, 2):
                right_size = n - 1 - left_size
                left_trees = build(left_size)
                right_trees = build(right_size)
                for left in left_trees:
                    for right in right_trees:
                        root = TreeNode(0)
                        root.left = left
                        root.right = right
                        result.append(root)
            memo[n] = result
            return result
        return build(n)
def tree_to_list(root):
    if root is None:
        return None
    return [root.val, tree_to_list(root.left), tree_to_list(root.right)]
if __name__ == "__main__":
    sol = Solution()
    n1 = 7
    result1 = sol.allPossibleFBT(n1)
    print("Example 1: {} full binary trees generated for n=7 (expected 5)".format(len(result1)))
    for tree in result1:
        print("  ", tree_to_list(tree))
    print()
    n2 = 3
    result2 = sol.allPossibleFBT(n2)
    print("Example 2: {} full binary trees generated for n=3 (expected 1)".format(len(result2)))
    for tree in result2:
        print("  ", tree_to_list(tree))
    print()
    n3 = 1
    result3 = sol.allPossibleFBT(n3)
    print("Example 3 (n=1): {} tree(s)".format(len(result3)))
    for tree in result3:
        print("  ", tree_to_list(tree))
    n4 = 2
    result4 = sol.allPossibleFBT(n4)
    print("Example 4 (n=2, even): {} tree(s) (expected 0)".format(len(result4)))