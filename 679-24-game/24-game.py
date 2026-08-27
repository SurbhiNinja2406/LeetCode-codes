from itertools import permutations
class Solution(object):
    def judgePoint24(self, cards):
        """
        :type cards: List[int]
        :rtype: bool
        """
        EPS = 1e-6
        TARGET = 24.0
        def solve(nums):
            if len(nums) == 1:
                return abs(nums[0] - TARGET) < EPS
            n = len(nums)
            for i in range(n):
                for j in range(n):
                    if i == j:
                        continue
                    rest = [nums[k] for k in range(n) if k != i and k != j]
                    a, b = nums[i], nums[j]
                    candidates = [a + b, a - b, a * b]
                    if abs(b) > EPS:
                        candidates.append(a / b)
                    for value in candidates:
                        if solve(rest + [value]):
                            return True
            return False
        return solve([float(c) for c in cards])
if __name__ == "__main__":
    solution = Solution()
    result1 = solution.judgePoint24([4, 1, 8, 7])
    print("Example 1:")
    print("Input:  cards = [4,1,8,7]")
    print("Output:", result1)
    print("Expected: True")
    print()
    result2 = solution.judgePoint24([1, 2, 1, 2])
    print("Example 2:")
    print("Input:  cards = [1,2,1,2]")
    print("Output:", result2)
    print("Expected: False")
    print()
    result3 = solution.judgePoint24([8, 8, 3, 3])
    print("Example 3 (extra):")
    print("Input:  cards = [8,8,3,3]")
    print("Output:", result3)
    print("Expected: True")
    print()
    result4 = solution.judgePoint24([6, 6, 6, 6])
    print("Example 4 (extra):")
    print("Input:  cards = [6,6,6,6]")
    print("Output:", result4)
    print("Expected: True")
    print()
    result5 = solution.judgePoint24([1, 1, 1, 1])
    print("Example 5 (extra):")
    print("Input:  cards = [1,1,1,1]")
    print("Output:", result5)
    print("Expected: False")
    print()
    result6 = solution.judgePoint24([9, 9, 9, 9])
    print("Example 6 (extra):")
    print("Input:  cards = [9,9,9,9]")
    print("Output:", result6)
print(__name__)