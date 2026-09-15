from collections import Counter
import math
class Solution(object):
    def numSquarefulPerms(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        def is_perfect_square(x):
            root = int(math.sqrt(x))
            return root * root == x or (root + 1) * (root + 1) == x
        count = Counter(nums)
        distinct_vals = list(count.keys())
        can_follow = {v: [] for v in distinct_vals}
        for v1 in distinct_vals:
            for v2 in distinct_vals:
                if is_perfect_square(v1 + v2):
                    can_follow[v1].append(v2)
        self.result = 0
        def backtrack(current_val, remaining):
            if remaining == 0:
                self.result += 1
                return
            for next_val in can_follow[current_val]:
                if count[next_val] > 0:
                    count[next_val] -= 1
                    backtrack(next_val, remaining - 1)
                    count[next_val] += 1
        for start_val in distinct_vals:
            count[start_val] -= 1
            backtrack(start_val, n - 1)
            count[start_val] += 1
        return self.result
if __name__ == "__main__":
    sol = Solution()
    print(sol.numSquarefulPerms([1, 17, 8]))  
    print(sol.numSquarefulPerms([2, 2, 2]))  
print(__name__)