class Solution(object):
    def numSubarrayProductLessThanK(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        if k <= 1:
            return 0
        count = 0
        product = 1
        left = 0
        for right in range(len(nums)):
            product *= nums[right]
            while product >= k:
                product //= nums[left]
                left += 1
            count += right - left + 1
        return count
if __name__ == "__main__":
    sol = Solution()
    print(sol.numSubarrayProductLessThanK([10, 5, 2, 6], 100))
    print("Expected: 8\n")
    print(sol.numSubarrayProductLessThanK([1, 2, 3], 0))
    print("Expected: 0\n")
    print(sol.numSubarrayProductLessThanK([1, 1, 1], 1))
    print("Expected: 0\n")
    print(sol.numSubarrayProductLessThanK([5], 10))
    print("Expected: 1\n")
    print(sol.numSubarrayProductLessThanK([5], 5))
    print("Expected: 0\n")
    print(sol.numSubarrayProductLessThanK([1, 1, 1], 1000))
    print("Expected: 6")  
print(__name__)