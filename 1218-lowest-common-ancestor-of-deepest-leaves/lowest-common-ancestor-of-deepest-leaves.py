# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def lcaDeepestLeaves(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: Optional[TreeNode]
        """
        def dfs(node):
            if node is None:
                return None, 0            
            left_node, left_depth = dfs(node.left)
            right_node, right_depth = dfs(node.right)            
            if left_depth == right_depth:
                return node, left_depth + 1
            elif left_depth > right_depth:
                return left_node, left_depth + 1
            else:
                return right_node, right_depth + 1        
        lca, _ = dfs(root)
        return lca
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
def tree_to_list(node):
    if node is None:
        return []    
    from collections import deque    
    result = []
    queue = deque([node])    
    while queue:
        current = queue.popleft()
        if current is None:
            result.append(None)
        else:
            result.append(current.val)
            queue.append(current.left)
            queue.append(current.right)
    while result and result[-1] is None:
        result.pop()    
    return result

if __name__ == "__main__":
    solution = Solution()
    root1 = build_tree([3, 5, 1, 6, 2, 0, 8, None, None, 7, 4])
    result1 = solution.lcaDeepestLeaves(root1)
    print("Example 1: {} (Expected: [2,7,4])".format(tree_to_list(result1)))
    root2 = build_tree([1])
    result2 = solution.lcaDeepestLeaves(root2)
    print("Example 2: {} (Expected: [1])".format(tree_to_list(result2)))
    root3 = build_tree([0, 1, 3, None, 2])
    result3 = solution.lcaDeepestLeaves(root3)
    print("Example 3: {} (Expected: [2])".format(tree_to_list(result3)))
print(__name__)