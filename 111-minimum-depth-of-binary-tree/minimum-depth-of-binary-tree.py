# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def minDepth(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        if root is None:
            return 0
        queue = deque([(root, 1)])  
        while queue:
            node, depth = queue.popleft()
            if node.left is None and node.right is None:
                return depth 
            if node.left:
                queue.append((node.left, depth + 1))
            if node.right:
                queue.append((node.right, depth + 1))
        return 0 
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
    root1 = build_tree([3, 9, 20, None, None, 15, 7])
    print("Test 1: {}".format(sol.minDepth(root1))) 
    root2 = build_tree([2, None, 3, None, 4, None, 5, None, 6])
    print("Test 2: {}".format(sol.minDepth(root2))) 
print(__name__)