class Solution(object):
    def smallestDistancePair(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        nums.sort()
        n = len(nums)
        def count_pairs_with_distance_at_most(mid):
            count = 0
            left = 0
            for right in range(n):
                while nums[right] - nums[left] > mid:
                    left += 1
                count += right - left
            return count
        lo, hi = 0, nums[-1] - nums[0]
        while lo < hi:
            mid = (lo + hi) // 2
            if count_pairs_with_distance_at_most(mid) >= k:
                hi = mid
            else:
                lo = mid + 1
        return lo
if __name__ == "__main__":
    sol = Solution()
    print(sol.smallestDistancePair([1, 3, 1], 1))
    print("Expected: 0\n")
    print(sol.smallestDistancePair([1, 1, 1], 2))
    print("Expected: 0\n")
    print(sol.smallestDistancePair([1, 6, 1], 3))
    print("Expected: 5\n")
    print(sol.smallestDistancePair([5, 10], 1))
    print("Expected: 5\n")
    import itertools
    nums_test = [9, 10, 7, 10, 6, 1, 5, 4, 9, 8]
    all_pairs = sorted(abs(a - b) for a, b in itertools.combinations(nums_test, 2))
    for k_test in [1, 5, 15, len(all_pairs)]:
        result = sol.smallestDistancePair(nums_test[:], k_test)
        expected = all_pairs[k_test - 1]
        print("k={0}: got {1}, expected {2}, match={3}".format(
            k_test, result, expected, result == expected))