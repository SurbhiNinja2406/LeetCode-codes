class Solution(object):
    def missingElement(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        n = len(nums)
        def missing(i):
            return nums[i] - nums[0] - i
        if k > missing(n - 1):
            return nums[-1] + k - missing(n - 1)
        left, right = 0, n - 1
        while left < right:
            mid = (left + right) // 2
            if missing(mid) < k:
                left = mid + 1
            else:
                right = mid
        return nums[left - 1] + k - missing(left - 1)
if __name__ == "__main__":
    sol = Solution()
    print(sol.missingElement([4, 7, 9, 10], 1)) 
    print(sol.missingElement([4, 7, 9, 10], 3))  
    print(sol.missingElement([1, 2, 4], 3))   
print(__name__)