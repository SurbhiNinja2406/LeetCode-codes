class Solution(object):
    def sortArrayByParityII(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        result = [0] * n
        even_idx = 0  
        odd_idx = 1 
        for num in nums:
            if num % 2 == 0:
                result[even_idx] = num
                even_idx += 2
            else:
                result[odd_idx] = num
                odd_idx += 2
        return result
if __name__ == "__main__":
    sol = Solution()
    print(sol.sortArrayByParityII([4, 2, 5, 7]))
    print(sol.sortArrayByParityII([2, 3]))
print(__name__)