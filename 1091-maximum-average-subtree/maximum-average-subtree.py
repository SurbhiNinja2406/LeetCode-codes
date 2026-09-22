# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def maximumAverageSubtree(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: float
        """
        self.max_avg = float('-inf')        
        self._dfs(root)        
        return self.max_avg    
    def _dfs(self, node):
        """
        Returns (sum_of_subtree, count_of_nodes) for the subtree rooted at node.
        Updates self.max_avg along the way.
        """
        if node is None:
            return 0, 0        
        left_sum, left_count = self._dfs(node.left)
        right_sum, right_count = self._dfs(node.right)        
        total_sum = left_sum + right_sum + node.val
        total_count = left_count + right_count + 1        
        avg = float(total_sum) / total_count
        self.max_avg = max(self.max_avg, avg)        
        return total_sum, total_count
def build_tree(values):
    if not values or values[0] is None:
        return None    
    from collections import deque    
    root = TreeNode(values[0])
    queue = deque([root])
    i = 1    
    while queue and i < len(values):
        node = queue.popleft()        
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
if __name__ == "__main__":
    solution = Solution()
    root1 = build_tree([5, 6, 1])
    result1 = solution.maximumAverageSubtree(root1)
    print("Example 1: {:.5f} (Expected: 6.00000)".format(result1))
    root2 = build_tree([0, None, 1])
    result2 = solution.maximumAverageSubtree(root2)
    print("Example 2: {:.5f} (Expected: 1.00000)".format(result2))