class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        result = []
        combo = []
        def backtrack(start):
            if len(combo) == k:
                result.append(combo[:])
                return
            remaining_needed = k - len(combo)
            for num in range(start, n - remaining_needed + 2):
                combo.append(num)
                backtrack(num + 1)
                combo.pop() 
        backtrack(1)
        return result
if __name__ == "__main__":
    sol = Solution()
    print(sol.combine(4, 2))  
    print(sol.combine(1, 1)) 
print(__name__)