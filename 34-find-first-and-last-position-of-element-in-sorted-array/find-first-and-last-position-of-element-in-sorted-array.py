class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        def find_leftmost(nums, target):
            lo, hi = 0, len(nums) - 1
            result = -1
            while lo <= hi:
                mid = (lo + hi) // 2
                if nums[mid] == target:
                    result = mid
                    hi = mid - 1 
                elif nums[mid] < target:
                    lo = mid + 1
                else:
                    hi = mid - 1
            return result
        def find_rightmost(nums, target):
            lo, hi = 0, len(nums) - 1
            result = -1
            while lo <= hi:
                mid = (lo + hi) // 2
                if nums[mid] == target:
                    result = mid
                    lo = mid + 1  
                elif nums[mid] < target:
                    lo = mid + 1
                else:
                    hi = mid - 1
            return result
        left = find_leftmost(nums, target)
        if left == -1:
            return [-1, -1]
        right = find_rightmost(nums, target)
        return [left, right]
if __name__ == "__main__":
    sol = Solution()
    print(sol.searchRange([5, 7, 7, 8, 8, 10], 8)) 
    print(sol.searchRange([5, 7, 7, 8, 8, 10], 6))  
    print(sol.searchRange([], 0)) 
    print(sol.searchRange([5], 5))  
    print(sol.searchRange([5], 3)) 
    print(sol.searchRange([2, 2, 2, 2, 2], 2))  
    print(sol.searchRange([1, 2, 3, 4, 5], 1)) 
    print(sol.searchRange([1, 2, 3, 4, 5], 5))
    print(sol.searchRange([5, 6, 7], 2))  
    print(sol.searchRange([5, 6, 7], 10)) 
print(__name__)