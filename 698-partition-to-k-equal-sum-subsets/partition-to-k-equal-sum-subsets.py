class Solution(object):
    def canPartitionKSubsets(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        total = sum(nums)
        if total % k != 0:
            return False
        target = total // k
        n = len(nums)
        nums.sort(reverse=True)  
        if nums[0] > target:
            return False
        memo = {}  
        def dfs(mask, curr_sum, buckets_left):
            if buckets_left == 0:
                return True
            if curr_sum == target:
                result = dfs(mask, 0, buckets_left - 1)
                return result
            if mask in memo:
                return False  
            for i in range(n):
                if mask & (1 << i):
                    continue  
                if curr_sum + nums[i] > target:
                    continue  
                if dfs(mask | (1 << i), curr_sum + nums[i], buckets_left):
                    return True
                while i + 1 < n and nums[i + 1] == nums[i]:
                    i += 1
            memo[mask] = False
            return False
        return dfs(0, 0, k)
if __name__ == "__main__":
    sol = Solution()
    print(sol.canPartitionKSubsets([4,3,2,3,5,2,1], 4))  
    print(sol.canPartitionKSubsets([1,2,3,4], 3))  
print(__name__)