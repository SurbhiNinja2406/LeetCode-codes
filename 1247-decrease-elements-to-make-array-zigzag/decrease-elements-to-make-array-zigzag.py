class Solution(object):
    def movesToMakeZigzag(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)        
        def cost(make_even_peaks):
            total = 0
            for i in range(n):
                is_valley = (i % 2 == 0) if not make_even_peaks else (i % 2 == 1)                
                if is_valley:
                    left = nums[i - 1] if i - 1 >= 0 else float('inf')
                    right = nums[i + 1] if i + 1 < n else float('inf')
                    min_neighbor = min(left, right)
                    if nums[i] >= min_neighbor:
                        total += nums[i] - min_neighbor + 1            
            return total
        return min(cost(True), cost(False))
if __name__ == "__main__":
    sol = Solution()
    print(sol.movesToMakeZigzag([1, 2, 3]))  
    print(sol.movesToMakeZigzag([9, 6, 1, 6, 2])) 
print(__name__)