# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def splitBST(self, root, target):
        """
        :type root: Optional[TreeNode]
        :type target: int
        :rtype: List[Optional[TreeNode]]
        """
        if root is None:
            return [None, None]
        if root.val <= target:
            smaller, greater = self.splitBST(root.right, target)
            root.right = smaller
            return [root, greater]
        else:
            smaller, greater = self.splitBST(root.left, target)
            root.left = greater
            return [smaller, root]
    def buildTree(self, values):
        if not values or values[0] is None:
            return None
        nodes = [None if v is None else TreeNode(v) for v in values]
        kids = nodes[::-1]
        root = kids.pop()
        for node in nodes:
            if node:
                if kids:
                    node.left = kids.pop()
                if kids:
                    node.right = kids.pop()
        return root
    def treeToList(self, root):
        if root is None:
            return []
        result = []
        queue = [root]
        while queue:
            node = queue.pop(0)
            if node is None:
                result.append(None)
            else:
                result.append(node.val)
                queue.append(node.left)
                queue.append(node.right)
        while result and result[-1] is None:
            result.pop()
        return result
if __name__ == "__main__":
    sol = Solution()
    root = sol.buildTree([4, 2, 6, 1, 3, 5, 7])
    target = 2
    result = sol.splitBST(root, target)
    output = [sol.treeToList(r) for r in result]
    print("Input: root = [4,2,6,1,3,5,7], target = {}".format(target))
    print("Output: {}".format(output))
    print("Expected: [[2, 1], [4, 3, 6, None, None, 5, 7]]\n")
    root = sol.buildTree([1])
    target = 1
    result = sol.splitBST(root, target)
    output = [sol.treeToList(r) for r in result]
    print("Input: root = [1], target = {}".format(target))
    print("Output: {}".format(output))
    print("Expected: [[1], []]\n")