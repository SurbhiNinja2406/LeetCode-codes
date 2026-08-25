# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if not head:
            return False        
        slow = head
        fast = head        
        while fast and fast.next:
            slow = slow.next         
            fast = fast.next.next    
            if slow == fast:
                return True        
        return False
def build_linked_list(values, pos):
    if not values:
        return None    
    nodes = [ListNode(v) for v in values]
    for i in range(len(nodes) - 1):
        nodes[i].next = nodes[i + 1]    
    if pos != -1:
        nodes[-1].next = nodes[pos]    
    return nodes[0]
if __name__ == "__main__":
    sol = Solution()
    head1 = build_linked_list([3, 2, 0, -4], 1)
    print(sol.hasCycle(head1)) 
    head2 = build_linked_list([1, 2], 0)
    print(sol.hasCycle(head2))  
    head3 = build_linked_list([1], -1)
    print(sol.hasCycle(head3)) 
print(__name__)