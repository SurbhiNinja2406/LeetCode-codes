class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        total = sum(nums)
        left_sum = 0
        for i, num in enumerate(nums):
            if left_sum == total - left_sum - num:
                return i
            left_sum += num
        return -1


if __name__ == "__main__":
    sol = Solution()
    print(sol.pivotIndex([1, 7, 3, 6, 5, 6]))
    print("Expected: 3\n")
    print(sol.pivotIndex([1, 2, 3]))
    print("Expected: -1\n")
    print(sol.pivotIndex([2, 1, -1]))
    print("Expected: 0\n")
    print(sol.pivotIndex([5]))
    print("Expected: 0\n")
    print(sol.pivotIndex([-1, -1, -1, 0, 1, 1]))
    print("Expected: 5\n")
    print(sol.pivotIndex([0, 0, 0, 0]))
    print("Expected: 0")
print(__name__)