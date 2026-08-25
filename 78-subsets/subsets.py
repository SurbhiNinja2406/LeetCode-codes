class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = [[]]
        for num in nums:
            result += [subset + [num] for subset in result]
        return result
if __name__ == "__main__":
    sol = Solution()
    print(sol.subsets([1, 2, 3]))
    print(sol.subsets([0]))