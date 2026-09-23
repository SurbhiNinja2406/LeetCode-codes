import bisect
class Solution(object):
    def isMajorityElement(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """
        n = len(nums)
        left = bisect.bisect_left(nums, target)  
        right = bisect.bisect_right(nums, target)  
        count = right - left        
        return count > n // 2
if __name__ == "__main__":
    sol = Solution()
    print(sol.isMajorityElement([2,4,5,5,5,5,5,6,6], 5))   
    print(sol.isMajorityElement([10,100,101,101], 101))   
print(__name__)