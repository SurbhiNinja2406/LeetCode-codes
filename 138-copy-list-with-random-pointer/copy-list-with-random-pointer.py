# Definition for a Node.
class Node:
    def __init__(self, x, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random
class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        if not head:
            return None
        old_to_new = {}
        current = head
        while current:
            old_to_new[current] = Node(current.val)
            current = current.next
        current = head
        while current:
            clone = old_to_new[current]
            clone.next = old_to_new[current.next] if current.next else None
            clone.random = old_to_new[current.random] if current.random else None
            current = current.next        
        return old_to_new[head]
def build_list(pairs):
    if not pairs:
        return None    
    nodes = [Node(val) for val, _ in pairs]    
    for i in range(len(nodes) - 1):
        nodes[i].next = nodes[i + 1]    
    for i, (val, random_index) in enumerate(pairs):
        if random_index is not None:
            nodes[i].random = nodes[random_index]    
    return nodes[0] if nodes else None
def list_to_pairs(head):
    nodes = []
    current = head
    index_map = {}    
    i = 0
    while current:
        index_map[current] = i
        nodes.append(current)
        current = current.next
        i += 1    
    result = []
    for node in nodes:
        random_index = index_map[node.random] if node.random else None
        result.append([node.val, random_index])    
    return result
if __name__ == "__main__":
    sol = Solution()
    pairs1 = [[7, None], [13, 0], [11, 4], [10, 2], [1, 0]]
    head1 = build_list(pairs1)
    cloned1 = sol.copyRandomList(head1)
    print(list_to_pairs(cloned1))
    pairs2 = [[1, 1], [2, 1]]
    head2 = build_list(pairs2)
    cloned2 = sol.copyRandomList(head2)
    print(list_to_pairs(cloned2))
    pairs3 = [[3, None], [3, 0], [3, None]]
    head3 = build_list(pairs3)
    cloned3 = sol.copyRandomList(head3)
    print(list_to_pairs(cloned3))
print(__name__)