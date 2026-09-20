class Solution(object):
    def validSubarrays(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        stack = []  
        count = 0
        for i in range(n):
            while stack and nums[i] < nums[stack[-1]]:
                top = stack.pop()
                count += i - top
            stack.append(i)
        for top in stack:
            count += n - top
        return count
if __name__ == "__main__":
    sol = Solution()
    print(sol.validSubarrays([1, 4, 2, 5, 3])) 
    print(sol.validSubarrays([3, 2, 1]))     
    print(sol.validSubarrays([2, 2, 2]))    
print(__name__)