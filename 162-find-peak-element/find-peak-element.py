class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left, right = 0, len(nums) - 1        
        while left < right:
            mid = (left + right) // 2
            if nums[mid] > nums[mid + 1]:
                right = mid
            else:
                left = mid + 1
        return left
if __name__ == "__main__":
    solution = Solution()
    test_cases = [
        ([1, 2, 3, 1], [2]),              
        ([1, 2, 1, 3, 5, 6, 4], [1, 5]),   
        ([1], [0]),                         
        ([1, 2], [1]),                     
        ([2, 1], [0]),                     
        ([5, 4, 3, 2, 1], [0]),          
        ([1, 2, 3, 4, 5], [4]),           
        ([1, 3, 2, 4, 1], [1, 3]),       
    ]
    for nums, acceptable in test_cases:
        result = solution.findPeakElement(nums)
        status = "PASS" if result in acceptable else "FAIL"
        print("[{0}] nums={1} -> got index {2} (value={3}), acceptable indices={4}".format(
            status, nums, result, nums[result], acceptable
        ))
print(__name__)