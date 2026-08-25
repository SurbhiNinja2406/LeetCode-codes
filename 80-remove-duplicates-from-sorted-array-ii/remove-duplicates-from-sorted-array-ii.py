class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) <= 2:
            return len(nums)
        k = 2 
        for i in range(2, len(nums)):
            if nums[i] != nums[k - 2]:
                nums[k] = nums[i]
                k += 1
        return k
if __name__ == "__main__":
    sol = Solution()
    nums1 = [1, 1, 1, 2, 2, 3]
    k1 = sol.removeDuplicates(nums1)
    print(k1, nums1[:k1]) 
    nums2 = [0, 0, 1, 1, 1, 1, 2, 3, 3]
    k2 = sol.removeDuplicates(nums2)
    print(k2, nums2[:k2])  