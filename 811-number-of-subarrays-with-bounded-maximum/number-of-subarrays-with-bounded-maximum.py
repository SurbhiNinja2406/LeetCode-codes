class Solution(object):
    def numSubarrayBoundedMax(self, nums, left, right):
        """
        :type nums: List[int]
        :type left: int
        :type right: int
        :rtype: int
        """
        def countAtMost(bound):
            count = 0
            current_len = 0 
            for num in nums:
                if num <= bound:
                    current_len += 1
                else:
                    current_len = 0  
                count += current_len
            return count
        return countAtMost(right) - countAtMost(left - 1)
if __name__ == "__main__":
    sol = Solution()
    print(sol.numSubarrayBoundedMax([2,1,4,3], 2, 3))  
    print(sol.numSubarrayBoundedMax([2,9,2,5,6], 2, 8)) 
print(__name__)