class Solution(object):
    def advantageCount(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        n = len(nums1)
        sorted_nums1 = sorted(nums1)
        sorted_nums2 = sorted(enumerate(nums2), key=lambda x: -x[1])        
        result = [0] * n        
        lo = 0         
        hi = n - 1       
        for original_idx, val in sorted_nums2:
            if sorted_nums1[hi] > val:
                result[original_idx] = sorted_nums1[hi]
                hi -= 1
            else:
                result[original_idx] = sorted_nums1[lo]
                lo += 1        
        return result
if __name__ == "__main__":
    sol = Solution()
    nums1_1, nums2_1 = [2, 7, 11, 15], [1, 10, 4, 11]
    result1 = sol.advantageCount(nums1_1, nums2_1)
    print("Example 1:")
    print("Input: nums1 = {}, nums2 = {}".format(nums1_1, nums2_1))
    print("Output:", result1)
    print("Expected: [2, 11, 7, 15]")
    print()
    nums1_2, nums2_2 = [12, 24, 8, 32], [13, 25, 32, 11]
    result2 = sol.advantageCount(nums1_2, nums2_2)
    print("Example 2:")
    print("Input: nums1 = {}, nums2 = {}".format(nums1_2, nums2_2))
    print("Output:", result2)
    print("Expected: [24, 32, 8, 12]")
    print()
    nums1_3, nums2_3 = [1, 2, 3], [10, 20, 30]
    result3 = sol.advantageCount(nums1_3, nums2_3)
    print("Additional test (no advantage possible):")
    print("Input: nums1 = {}, nums2 = {}".format(nums1_3, nums2_3))
    print("Output:", result3)
    print("(Any permutation is equally valid since no advantage is achievable)")
    print()
    nums1_4, nums2_4 = [5, 5, 5], [5, 5, 5]
    result4 = sol.advantageCount(nums1_4, nums2_4)
    print("Additional test (identical arrays):")
    print("Input: nums1 = {}, nums2 = {}".format(nums1_4, nums2_4))
    print("Output:", result4)
    print("Expected: [5, 5, 5] (no advantage possible either way)")
print(__name__)