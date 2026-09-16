class Solution(object):
    def sumEvenAfterQueries(self, nums, queries):
        """
        :type nums: List[int]
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        even_sum = sum(x for x in nums if x % 2 == 0)
        answer = []
        for val, index in queries:
            old_val = nums[index]
            if old_val % 2 == 0:
                even_sum -= old_val
            new_val = old_val + val
            nums[index] = new_val
            if new_val % 2 == 0:
                even_sum += new_val
            answer.append(even_sum)
        return answer
if __name__ == "__main__":
    sol = Solution()
    print(sol.sumEvenAfterQueries([1, 2, 3, 4], [[1, 0], [-3, 1], [-4, 0], [2, 3]])) 
    print(sol.sumEvenAfterQueries([1], [[4, 0]]))                                  
print(__name__)