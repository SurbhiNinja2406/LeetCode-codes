# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: Optional[TreeNode]
        :type q: Optional[TreeNode]
        :rtype: bool
        """
        if p is None and q is None:
            return True
        if p is None or q is None:
            return False
        if p.val != q.val:
            return False
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
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
    p1 = build_tree([1, 2, 3])
    q1 = build_tree([1, 2, 3])
    print("Test 1: {}".format(sol.isSameTree(p1, q1))) 
    p2 = build_tree([1, 2])
    q2 = build_tree([1, None, 2])
    print("Test 2: {}".format(sol.isSameTree(p2, q2)))  
    p3 = build_tree([1, 2, 1])
    q3 = build_tree([1, 1, 2])
    print("Test 3: {}".format(sol.isSameTree(p3, q3)))