class Node(object):
    def __init__(self, val=0, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
class Solution(object):
    def connect(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        if root is None:
            return None
        leftmost = root  
        while leftmost:
            dummy = Node(0)
            tail = dummy
            head = leftmost  
            while head:
                if head.left:
                    tail.next = head.left
                    tail = tail.next
                if head.right:
                    tail.next = head.right
                    tail = tail.next
                head = head.next
            leftmost = dummy.next
        return root
def build_tree(values):
    if not values or values[0] is None:
        return None
    root = Node(values[0])
    queue = [root]
    i = 1
    while queue and i < len(values):
        node = queue.pop(0)
        if i < len(values):
            if values[i] is not None:
                node.left = Node(values[i])
                queue.append(node.left)
            i += 1
        if i < len(values):
            if values[i] is not None:
                node.right = Node(values[i])
                queue.append(node.right)
            i += 1
    return root
def print_with_next(root):
    result = []
    level_start = root
    while level_start:
        node = level_start
        next_level_start = None
        while node:
            result.append(node.val)
            if next_level_start is None:
                if node.left:
                    next_level_start = node.left
                elif node.right:
                    next_level_start = node.right
            node = node.next
        result.append('#')
        level_start = next_level_start
    return result
if __name__ == "__main__":
    sol = Solution()
    root1 = build_tree([1, 2, 3, 4, 5, None, 7])
    sol.connect(root1)
    print("Test 1: {}".format(print_with_next(root1)))
    root2 = build_tree([])
    result2 = sol.connect(root2)
    print("Test 2: {}".format(print_with_next(result2) if result2 else []))  
print(__name__)