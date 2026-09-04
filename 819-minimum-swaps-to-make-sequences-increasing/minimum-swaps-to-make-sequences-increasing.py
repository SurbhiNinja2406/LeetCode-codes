class Solution(object):
    def minSwap(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: int
        """
        n = len(nums1)
        keep = 0   
        swap = 1   
        for i in range(1, n):
            new_keep = float('inf')
            new_swap = float('inf')
            if nums1[i] > nums1[i - 1] and nums2[i] > nums2[i - 1]:
                new_keep = min(new_keep, keep)
                new_swap = min(new_swap, swap + 1)
            if nums1[i] > nums2[i - 1] and nums2[i] > nums1[i - 1]:
                new_keep = min(new_keep, swap)
                new_swap = min(new_swap, keep + 1)
            keep, swap = new_keep, new_swap
        return min(keep, swap)
if __name__ == "__main__":
    solution = Solution()
    test_cases = [
        ([1, 3, 5, 4], [1, 2, 3, 7], 1),
        ([0, 3, 5, 8, 9], [2, 1, 4, 6, 9], 1),
    ]
    for nums1, nums2, expected in test_cases:
        result = solution.minSwap(list(nums1), list(nums2))
        status = "PASS" if result == expected else "FAIL"
        print("nums1={:<18} nums2={:<18} expected={} got={} [{}]".format(
            str(nums1), str(nums2), expected, result, status))
print(__name__)