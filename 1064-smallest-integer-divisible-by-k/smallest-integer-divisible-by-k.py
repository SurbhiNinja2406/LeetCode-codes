class Solution(object):
    def smallestRepunitDivByK(self, k):
        """
        :type k: int
        :rtype: int
        """
        if k % 2 == 0 or k % 5 == 0:
            return -1
        remainder = 0
        length = 0
        while True:
            remainder = (remainder * 10 + 1) % k
            length += 1
            if remainder == 0:
                return length
            if length > k:
                return -1
if __name__ == "__main__":
    sol = Solution()
    test_cases = [
        (1, 1),
        (2, -1),
        (3, 3),
        (7, 6),
        (9, 9),
        (100000, -1),
    ]
    for k, expected in test_cases:
        result = sol.smallestRepunitDivByK(k)
        status = "PASS" if result == expected else "FAIL"
        print("k={0} -> {1} (expected {2}) [{3}]".format(
            k, result, expected, status
        ))