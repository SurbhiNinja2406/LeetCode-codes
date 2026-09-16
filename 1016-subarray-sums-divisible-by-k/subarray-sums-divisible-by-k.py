class Solution(object):
    def subarraysDivByK(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        count = [0] * k
        count[0] = 1 
        prefix_sum = 0
        result = 0
        for num in nums:
            prefix_sum += num
            remainder = prefix_sum % k
            result += count[remainder]
            count[remainder] += 1
        return result
if __name__ == "__main__":
    sol = Solution()
    print(sol.subarraysDivByK([4, 5, 0, -2, -3, 1], 5))  
    print(sol.subarraysDivByK([5], 9))               
print(__name__)