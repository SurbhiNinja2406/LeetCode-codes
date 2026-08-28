class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        lo, hi = 0, len(nums) - 1
        while lo <= hi:
            mid = lo + (hi - lo) // 2  
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                lo = mid + 1
            else:
                hi = mid - 1
        return -1
if __name__ == "__main__":
    sol = Solution()
    print(sol.search([-1, 0, 3, 5, 9, 12], 9)) 
    print(sol.search([-1, 0, 3, 5, 9, 12], 2)) 
print(__name__)