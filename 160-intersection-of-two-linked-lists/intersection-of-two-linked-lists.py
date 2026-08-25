# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        if not headA or not headB:
            return None

        pointerA = headA
        pointerB = headB

        # Two pointers each traverse both lists in sequence: A then B,
        # and B then A. If the lists intersect, both pointers will
        # meet exactly at the intersection node after at most m + n steps,
        # because by that point they've each walked the same total distance.
        # If the lists don't intersect, both pointers will simultaneously
        # become None after walking m + n steps, and the loop ends
        # with pointerA == pointerB == None.
        while pointerA is not pointerB:
            pointerA = pointerA.next if pointerA else headB
            pointerB = pointerB.next if pointerB else headA

        return pointerA


# ---------- helper functions for testing ----------

def build_intersecting_lists(listA_vals, listB_vals, skipA, skipB):
    """
    Builds two linked lists that intersect at the point described by
    skipA/skipB, mirroring how the judge constructs test cases.
    listA_vals and listB_vals already include the shared/intersecting
    tail values at the end.
    """
    nodesA = [ListNode(v) for v in listA_vals]
    for i in range(len(nodesA) - 1):
        nodesA[i].next = nodesA[i + 1]
    nodesB = [ListNode(v) for v in listB_vals[:skipB]]  
    for i in range(len(nodesB) - 1):
        nodesB[i].next = nodesB[i + 1]
    if skipA < len(nodesA):
        intersection_node = nodesA[skipA]
        if nodesB:
            nodesB[-1].next = intersection_node
        else:
            nodesB_head = intersection_node
    else:
        intersection_node = None
    headA = nodesA[0] if nodesA else None
    headB = nodesB[0] if nodesB else (intersection_node if not nodesB else None)
    return headA, headB, intersection_node
if __name__ == "__main__":
    obj = Solution()
    common = [ListNode(8), ListNode(4), ListNode(5)]
    common[0].next = common[1]
    common[1].next = common[2]
    a_prefix = [ListNode(4), ListNode(1)]
    a_prefix[0].next = a_prefix[1]
    a_prefix[1].next = common[0]
    headA1 = a_prefix[0]
    b_prefix = [ListNode(5), ListNode(6), ListNode(1)]
    b_prefix[0].next = b_prefix[1]
    b_prefix[1].next = b_prefix[2]
    b_prefix[2].next = common[0]
    headB1 = b_prefix[0]
    result1 = obj.getIntersectionNode(headA1, headB1)
    print("Intersected at:", result1.val if result1 else None)  
    common2 = [ListNode(2), ListNode(4)]
    common2[0].next = common2[1]
    a_prefix2 = [ListNode(1), ListNode(9), ListNode(1)]
    a_prefix2[0].next = a_prefix2[1]
    a_prefix2[1].next = a_prefix2[2]
    a_prefix2[2].next = common2[0]
    headA2 = a_prefix2[0]
    b_prefix2 = [ListNode(3)]
    b_prefix2[0].next = common2[0]
    headB2 = b_prefix2[0]
    result2 = obj.getIntersectionNode(headA2, headB2)
    print("Intersected at:", result2.val if result2 else None) 
    a3 = [ListNode(2), ListNode(6), ListNode(4)]
    a3[0].next = a3[1]
    a3[1].next = a3[2]
    headA3 = a3[0]
    b3 = [ListNode(1), ListNode(5)]
    b3[0].next = b3[1]
    headB3 = b3[0]
    result3 = obj.getIntersectionNode(headA3, headB3)
    print("Intersected at:", result3.val if result3 else None)  