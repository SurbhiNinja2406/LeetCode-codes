# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator(object):

    def __init__(self, root):
        """
        :type root: Optional[TreeNode]
        """
        self.stack = []
        self._push_left(root)
    def _push_left(self, node):
        """
        Helper method: pushes a node and all its left descendants
        onto the stack, since in in-order traversal, we must visit
        the leftmost node first.
        """
        while node:
            self.stack.append(node)
            node = node.left
    def next(self):
        """
        :rtype: int
        """
        node = self.stack.pop()
        if node.right:
            self._push_left(node.right)
        return node.val
    def hasNext(self):
        """
        :rtype: bool
        """
        return len(self.stack) > 0
if __name__ == "__main__":
    root = TreeNode(7)
    root.left = TreeNode(3)
    root.right = TreeNode(15)
    root.right.left = TreeNode(9)
    root.right.right = TreeNode(20)
    bSTIterator = BSTIterator(root)
    print(bSTIterator.next())     
    print(bSTIterator.next())    
    print(bSTIterator.hasNext())  
    print(bSTIterator.next())    
    print(bSTIterator.hasNext())  
    print(bSTIterator.next())    
    print(bSTIterator.hasNext()) 
    print(bSTIterator.next())     
    print(bSTIterator.hasNext())
print(__name__)
# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()