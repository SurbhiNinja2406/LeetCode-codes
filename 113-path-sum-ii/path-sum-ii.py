# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def pathSum(self, root, targetSum):
        """
        :type root: Optional[TreeNode]
        :type targetSum: int
        :rtype: List[List[int]]
        """
        result = []
        path = []
        def dfs(node, remaining):
            if node is None:
                return
            path.append(node.val)
            remaining -= node.val
            if node.left is None and node.right is None and remaining == 0:
                result.append(list(path)) 
            else:
                dfs(node.left, remaining)
                dfs(node.right, remaining)
            path.pop()
        dfs(root, targetSum)
        return result
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
if __name__ == "__main__":
    sol = Solution()
    root1 = build_tree([5, 4, 8, 11, None, 13, 4, 7, 2, None, None, 5, 1])
    print("Test 1: {}".format(sol.pathSum(root1, 22)))  
    root2 = build_tree([1, 2, 3])
    print("Test 2: {}".format(sol.pathSum(root2, 5))) 
    root3 = build_tree([1, 2])
    print("Test 3: {}".format(sol.pathSum(root3, 0)))
print(__name__)