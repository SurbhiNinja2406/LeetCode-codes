# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def isCousins(self, root, x, y):
        """
        :type root: Optional[TreeNode]
        :type x: int
        :type y: int
        :rtype: bool
        """
        if not root:
            return False
        queue = [root]
        while queue:
            found_x = False
            found_y = False
            next_queue = []
            for node in queue:
                left = node.left
                right = node.right
                if left and right:
                    if (left.val == x and right.val == y) or (left.val == y and right.val == x):
                        return False  
                if node.val == x:
                    found_x = True
                if node.val == y:
                    found_y = True
                if left:
                    next_queue.append(left)
                if right:
                    next_queue.append(right)
            if found_x and found_y:
                return True
            if found_x or found_y:
                return False  
            queue = next_queue
        return False
def build_tree(values):
    if not values or values[0] is None:
        return None
    nodes = [None if v is None else TreeNode(v) for v in values]
    kids = nodes[::-1]
    root = kids.pop()
    for node in nodes:
        if node:
            if kids:
                child = kids.pop()
                node.left = child
            if kids:
                child = kids.pop()
                node.right = child
    return root
if __name__ == "__main__":
    sol = Solution()
    root1 = build_tree([1, 2, 3, 4])
    print(sol.isCousins(root1, 4, 3))  
    root2 = build_tree([1, 2, 3, None, 4, None, 5])
    print(sol.isCousins(root2, 5, 4)) 
    root3 = build_tree([1, 2, 3, None, 4])
    print(sol.isCousins(root3, 2, 3))  
print(__name__)