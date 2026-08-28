class Solution(object):
    def findShortestSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        first = {}  
        last = {}  
        count = {}  
        for i, num in enumerate(nums):
            if num not in first:
                first[num] = i
            last[num] = i
            count[num] = count.get(num, 0) + 1
        max_degree = max(count.values())
        result = float('inf')
        for num in count:
            if count[num] == max_degree:
                span = last[num] - first[num] + 1
                result = min(result, span)
        return result
if __name__ == "__main__":
    sol = Solution()
    print(sol.findShortestSubArray([1, 2, 2, 3, 1]))         
    print(sol.findShortestSubArray([1, 2, 2, 3, 1, 4, 2]))  
print(__name__)