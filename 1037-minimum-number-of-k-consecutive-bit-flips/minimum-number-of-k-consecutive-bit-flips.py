class Solution(object):
    def minKBitFlips(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        n = len(nums)
        diff = [0] * (n + 1)
        current_flip = 0  
        count = 0
        for i in range(n):
            current_flip += diff[i]
            effective_val = (nums[i] + current_flip) % 2
            if effective_val == 0:
                if i + k > n:
                    return -1  
                count += 1
                current_flip += 1
                diff[i + k] -= 1 
        return count
if __name__ == "__main__":
    sol = Solution()
    print(sol.minKBitFlips([0, 1, 0], 1)) 
    print(sol.minKBitFlips([1, 1, 0], 2)) 
    print(sol.minKBitFlips([0, 0, 0, 1, 0, 1, 1, 0], 3)) 
print(__name__)