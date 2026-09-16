class Solution(object):
    def countTriplets(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        MAX_BIT = 16
        SIZE = 1 << MAX_BIT 
        cnt = [0] * SIZE
        for a in nums:
            for b in nums:
                cnt[a & b] += 1
        f = cnt[:]
        for bit in range(MAX_BIT):
            for mask in range(SIZE):
                if mask & (1 << bit):
                    f[mask] += f[mask ^ (1 << bit)]
        full_mask = SIZE - 1
        result = 0
        for num in nums:
            complement = num ^ full_mask  
            result += f[complement]
        return result
if __name__ == "__main__":
    sol = Solution()
    print(sol.countTriplets([2, 1, 3]))  
    print(sol.countTriplets([0, 0, 0])) 
print(__name__)