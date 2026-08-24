# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        dummy = ListNode(0)
        current = dummy
        while list1 is not None and list2 is not None:
            if list1.val <= list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next
            current = current.next
        current.next = list1 if list1 is not None else list2
        return dummy.next
def build_linked_list(values):
    dummy = ListNode(0)
    current = dummy
    for v in values:
        current.next = ListNode(v)
        current = current.next
    return dummy.next
def linked_list_to_list(node):
    result = []
    while node:
        result.append(node.val)
        node = node.next
    return result
if __name__ == "__main__":
    sol = Solution()
    list1 = build_linked_list([1, 2, 4])
    list2 = build_linked_list([1, 3, 4])
    result = sol.mergeTwoLists(list1, list2)
    print(linked_list_to_list(result)) 
    list1 = build_linked_list([])
    list2 = build_linked_list([])
    result = sol.mergeTwoLists(list1, list2)
    print(linked_list_to_list(result)) 
    list1 = build_linked_list([])
    list2 = build_linked_list([0])
    result = sol.mergeTwoLists(list1, list2)
    print(linked_list_to_list(result))  
    list1 = build_linked_list([1, 2, 3])
    list2 = build_linked_list([4, 5, 6])
    result = sol.mergeTwoLists(list1, list2)
    print(linked_list_to_list(result))  
    list1 = build_linked_list([4, 5, 6])
    list2 = build_linked_list([1, 2, 3])
    result = sol.mergeTwoLists(list1, list2)
    print(linked_list_to_list(result))  
    list1 = build_linked_list([1, 1, 1])
    list2 = build_linked_list([1, 1, 1])
    result = sol.mergeTwoLists(list1, list2)
    print(linked_list_to_list(result)) 
    list1 = build_linked_list([-5, -2, 0])
    list2 = build_linked_list([-3, -1, 1])
    result = sol.mergeTwoLists(list1, list2)
    print(linked_list_to_list(result)) 
print(__name__)