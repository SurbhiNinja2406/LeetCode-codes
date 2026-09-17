class Solution(object):
    def canThreePartsEqualSum(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        total = sum(arr)
        if total % 3 != 0:
            return False
        target = total // 3
        n = len(arr)
        current_sum = 0
        parts_found = 0
        for i in range(n):
            current_sum += arr[i]
            if current_sum == target and parts_found < 2:
                if parts_found == 1 and i == n - 1:
                    continue
                parts_found += 1
                current_sum = 0
        return parts_found == 2
if __name__ == "__main__":
    sol = Solution()
    test_cases = [
        ([0, 2, 1, -6, 6, -7, 9, 1, 2, 0, 1], True),
        ([0, 2, 1, -6, 6, 7, 9, -1, 2, 0, 1], False),
        ([3, 3, 6, 5, -2, 2, 5, 1, -9, 4], True),
        ([1, -1, 1, -1], False),
        ([1, 2, 3], False),
        ([0, 0, 0], True),
        ([1, -1, 1, -1, 1, -1], True),
    ]
    for arr, expected in test_cases:
        result = sol.canThreePartsEqualSum(arr)
        status = "PASS" if result == expected else "FAIL"
        print("arr={0} -> {1} (expected {2}) [{3}]".format(
            arr, result, expected, status
        ))