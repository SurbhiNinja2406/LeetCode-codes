class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ones, twos = 0, 0        
        for num in nums:
            ones = (ones ^ num) & ~twos
            twos = (twos ^ num) & ~ones
        return ones
if __name__ == "__main__":
    sol = Solution()
    nums1 = [2, 2, 3, 2]
    print(sol.singleNumber(nums1))  
    nums2 = [0, 1, 0, 1, 0, 1, 99]
    print(sol.singleNumber(nums2))  