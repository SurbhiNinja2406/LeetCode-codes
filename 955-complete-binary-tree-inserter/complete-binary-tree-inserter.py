# Definition for a binary tree node.
from collections import deque
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class CBTInserter(object):
    def __init__(self, root):
        """
        :type root: Optional[TreeNode]
        """
        self.root = root
        self.queue = deque()
        q = deque([root])
        while q:
            node = q.popleft()
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
            if not node.left or not node.right:
                self.queue.append(node)
    def insert(self, val):
        """
        :type val: int
        :rtype: int
        """
        new_node = TreeNode(val)
        parent = self.queue[0]
        if not parent.left:
            parent.left = new_node
        else:
            parent.right = new_node
            self.queue.popleft()
        self.queue.append(new_node)
        return parent.val
    def get_root(self):
        """
        :rtype: Optional[TreeNode]
        """
        return self.root
def build_tree_from_list(vals):
    if not vals:
        return None
    nodes = [TreeNode(v) if v is not None else None for v in vals]
    kids = nodes[::-1]
    root = kids.pop()
    for node in nodes:
        if node:
            if kids:
                node.left = kids.pop()
            if kids:
                node.right = kids.pop()
    return root
def tree_to_list(root):
    if not root:
        return []
    result = []
    q = deque([root])
    while q:
        node = q.popleft()
        result.append(node.val)
        if node.left:
            q.append(node.left)
        if node.right:
            q.append(node.right)
    return result
if __name__ == "__main__":
    root = build_tree_from_list([1, 2])
    cBTInserter = CBTInserter(root)
    print(None)                      
    print(cBTInserter.insert(3))      
    print(cBTInserter.insert(4))      
    print(tree_to_list(cBTInserter.get_root()))  
# Your CBTInserter object will be instantiated and called as such:
# obj = CBTInserter(root)
# param_1 = obj.insert(val)
# param_2 = obj.get_root()